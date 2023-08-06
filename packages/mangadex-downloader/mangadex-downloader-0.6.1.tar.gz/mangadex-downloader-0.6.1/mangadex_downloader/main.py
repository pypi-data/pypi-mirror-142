import logging
from pathvalidate import sanitize_filename
from pathlib import Path
from .utils import (
    Language,
    get_language,
    validate_url, 
    write_details,
    valid_cover_types,
    default_cover_type
)
from .utils import download as download_file
from .errors import InvalidURL, MangaDexException
from .fetcher import *
from .manga import Manga
from .chapter import Chapter
from .network import Net
from .format import default_save_as_format, get_format

log = logging.getLogger(__name__)

__all__ = (
    'download', 'download_chapter', 'download_list',
    'fetch', 'login', 'logout'
)

def login(*args, **kwargs):
    """Login to MangaDex

    Do not worry about token session, the library automatically handle this. 
    Login session will be automtically renewed (unless you called :meth:`logout()`).
    
    Parameters
    -----------
    password: :class:`str`
        Password to login
    username: Optional[:class:`str`]
        Username to login
    email: Optional[:class:`str`]
        Email to login
    
    Raises
    -------
    AlreadyLoggedIn
        User are already logged in
    ValueError
        Parameters are not valid
    LoginFailed
        Login credential are not valid
    """
    Net.requests.login(*args, **kwargs)

def logout():
    """Logout from MangaDex
    
    Raises
    -------
    NotLoggedIn
        User are not logged in
    """
    Net.requests.logout()

def _fetch_manga(manga_id, lang, fetch_relationships=True, fetch_all_chapters=True):
    data = get_manga(manga_id)

    if fetch_relationships:
        # Append some additional informations
        rels = data['data']['relationships']
        authors = []
        artists = []
        for rel in rels:
            _type = rel.get('type')
            _id = rel.get('id')

            if _type == 'author':
                log.debug('Getting author (%s) manga' % _id)
                authors.append(get_author(_id))

            elif _type == 'artist':
                log.debug('Getting artist (%s) manga' % _id)
                artists.append(get_author(_id))

            elif _type == 'cover_art':
                log.debug('Getting cover (%s) manga' % _id)
                data['cover_art'] = get_cover_art(_id)

        data['authors'] = authors
        data['artists'] = artists

    manga = Manga(data)

    if fetch_all_chapters:
        # NOTE: After v0.4.0, fetch the chapters first before creating folder for downloading the manga
        # and downloading the cover manga.
        # This will check if selected language in manga has chapters inside of it.
        # If the chapters are not available, it will throw error.
        log.info("Fetching all chapters...")
        chapters = Chapter(get_all_chapters(manga.id, lang), manga.title, lang)
        manga._chapters = chapters

    return manga

def fetch(url, language=Language.English):
    """Fetch the manga

    Parameters
    -----------
    url: :class:`str`
        A MangaDex URL or manga id
    language: :class:`Language` (default: :class:`Language.English`)
        Select a translated language for manga

    Raises
    -------
    InvalidURL
        Not a valid MangaDex url
    InvalidManga
        Given manga cannot be found
    ChapterNotFound
        Given manga has no chapters
    """
    # Parse language
    if isinstance(language, Language):
        lang = language.value
    elif isinstance(language, str):
        lang = get_language(language).value
    else:
        raise ValueError("language must be Language or str, not %s" % language.__class__.__name__)
    log.info("Using %s language" % Language(lang).name)

    log.debug('Validating the url...')
    try:
        manga_id = validate_url(url)
    except InvalidURL as e:
        log.error('%s is not valid mangadex url' % url)
        raise e from None
    
    # Begin fetching
    log.info('Fetching manga %s' % manga_id)
    manga = _fetch_manga(manga_id, lang)
    log.info("Found manga \"%s\"" % manga.title)

    return manga

def download(
    url,
    folder=None,
    replace=False,
    compressed_image=False,
    start_chapter=None,
    end_chapter=None,
    start_page=None,
    end_page=None,
    no_oneshot_chapter=False,
    language=Language.English,
    cover=default_cover_type,
    save_as=default_save_as_format
):
    """Download a manga
    
    Parameters
    -----------
    url: :class:`str`
        A MangaDex URL or manga id. It also accepting :class:`Manga` object
    folder: :class:`str` (default: ``None``)
        Store manga in given folder
    replace: :class:`bool` (default: ``False``)
        Replace manga if exist
    compressed_image: :class:`bool` (default: ``False``)
        Use compressed images for low size when downloading manga
    start_chapter: :class:`float` (default: ``None``)
        Start downloading manga from given chapter
    end_chapter: :class:`float` (default: ``None``)
        Stop downloading manga from given chapter
    start_page: :class:`int` (default: ``None``)
        Start download chapter page from given page number
    end_page: :class:`int` (default: ``None``)
        Stop download chapter page from given page number
    no_oneshot_manga: :class:`bool` (default: ``False``)
        If exist, don\'t download oneshot chapter
    language: :class:`Language` (default: :class:`Language.English`)
        Select a translated language for manga
    cover: :class:`str` (default: ``original``)
        Choose quality cover manga
    save_as: :class:`str` (default: ``tachiyomi``)
        Choose save as format

    Raises
    -------
    InvalidURL
        Not a valid MangaDex url
    InvalidManga
        Given manga cannot be found
    ChapterNotFound
        Given manga has no chapters
    """
    # Validate start_chapter and end_chapter param
    if start_chapter is not None and not isinstance(start_chapter, float):
        raise ValueError("start_chapter must be float, not %s" % type(start_chapter))
    if end_chapter is not None and not isinstance(end_chapter, float):
        raise ValueError("end_chapter must be float, not %s" % type(end_chapter))

    if start_chapter is not None and end_chapter is not None:
        if start_chapter > end_chapter:
            raise ValueError("start_chapter cannot be more than end_chapter")

    if cover not in valid_cover_types:
        raise ValueError("invalid cover type, available are: %s" % valid_cover_types)

    # Validation save as format
    fmt_class = get_format(save_as)

    if not isinstance(url, Manga):
        manga = fetch(url, language)
    else:
        manga = url

    # base path
    base_path = Path('.')

    # Extend the folder
    if folder:
        base_path /= folder
    base_path /= sanitize_filename(manga.title)
    
    # Create folder
    log.debug("Creating folder for downloading")
    base_path.mkdir(parents=True, exist_ok=True)

    # Cover path
    cover_path = base_path / 'cover.jpg'
    log.info('Downloading cover manga %s' % manga.title)

    # Determine cover art quality
    if cover == "original":
        cover_url = manga.cover_art
    elif cover == "512px":
        cover_url = manga.cover_art_512px
    elif cover == "256px":
        cover_url = manga.cover_art_256px
    elif cover == 'none':
        cover_url = None

    # Download the cover art
    if cover_url is None:
        log.debug('Not downloading cover manga, since \"cover\" is none')
    else:
        download_file(cover_url, str(cover_path), replace=True)

    kwargs_iter_chapter_images = {
        "start_chapter": start_chapter,
        "end_chapter": end_chapter,
        "start_page": start_page,
        "end_page": end_page,
        "no_oneshot": no_oneshot_chapter,
        "data_saver": compressed_image
    }

    log.info("Using %s format" % save_as)

    fmt = fmt_class(
        base_path,
        manga,
        compressed_image,
        replace,
        kwargs_iter_chapter_images
    )

    # Execute main format
    fmt.main()
                
    log.info("Download finished for manga \"%s\"" % manga.title)
    return manga

def download_chapter(
    url,
    folder=None,
    replace=False,
    start_page=None,
    end_page=None,
    compressed_image=False,
    save_as=default_save_as_format
):
    """Download a chapter
    
    Parameters
    -----------
    url: :class:`str`
        A MangaDex URL or chapter id
    folder: :class:`str` (default: ``None``)
        Store chapter manga in given folder
    replace: :class:`bool` (default: ``False``)
        Replace chapter manga if exist
    start_page: :class:`int` (default: ``None``)
        Start download chapter page from given page number
    end_page: :class:`int` (default: ``None``)
        Stop download chapter page from given page number
    compressed_image: :class:`bool` (default: ``False``)
        Use compressed images for low size when downloading chapter manga
    save_as: :class:`str` (default: ``tachiyomi``)
        Choose save as format
    """
    # Validate start_page and end_page param
    if start_page is not None and not isinstance(start_page, int):
        raise ValueError("start_page must be int, not %s" % type(start_page))
    if end_page is not None and not isinstance(end_page, int):
        raise ValueError("end_page must be int, not %s" % type(end_page))

    if start_page is not None and end_page is not None:
        if start_page > end_page:
            raise ValueError("start_page cannot be more than end_page")

    fmt_class = get_format(save_as)

    log.debug('Validating the url...')
    try:
        chap_id = validate_url(url)
    except InvalidURL as e:
        log.error('%s is not valid mangadex url' % url)
        raise e from None

    log.info("Fetching chapter %s" % chap_id)
    data = get_chapter(chap_id)
    vol = data['data']['attributes']['volume']
    if vol is None:
        vol = "none"
    chap = data['data']['attributes']['chapter']
    if chap is None:
        chap = "none"
    rels = data['data']['relationships']
    
    # Find manga id
    manga_id = None
    for rel in rels:
        _type = rel['type']
        _id = rel['id']
        if _type == "manga":
            manga_id = _id

    if manga_id is None:
        raise MangaDexException("chapter %s has no manga relationship" % chap_id)

    # For Chapter class
    parse_data = {
        "volumes": {
            vol: {
                "volume": vol,
                "chapters": {
                    chap: {
                        "chapter": chap,
                        "id": chap_id
                    }
                }
            }
        }
    }

    # Fetch manga
    manga = _fetch_manga(manga_id, "en", fetch_all_chapters=False)
    manga._chapters = Chapter(parse_data, manga.title, "en")
    log.info("Found chapter %s from manga \"%s\"" % (chap, manga.title))

    # base path
    base_path = Path('.')

    # Extend the folder
    if folder:
        base_path /= folder
    base_path /= sanitize_filename(manga.title)
    
    # Create folder
    log.debug("Creating folder for downloading")
    base_path.mkdir(parents=True, exist_ok=True)

    kwargs_iter_chapter_images = {
        "start_page": start_page,
        "end_page": end_page,
        "no_oneshot": False,
        "data_saver": compressed_image
    }

    log.info("Using %s format" % save_as)

    fmt = fmt_class(
        base_path,
        manga,
        compressed_image,
        replace,
        kwargs_iter_chapter_images
    )

    # Execute main format
    fmt.main()

    log.info("Finished download chapter %s from manga \"%s\"" % (chap, manga.title))
    return manga

def download_list(
    url,
    folder=None,
    replace=False,
    compressed_image=False,
    language=Language.English,
    cover=default_cover_type,
    save_as=default_save_as_format
):
    log.debug('Validating the url...')
    try:
        list_id = validate_url(url)
    except InvalidURL as e:
        log.error('%s is not valid mangadex url' % url)
        raise e from None

    data = get_list(list_id)
    name = data['data']['attributes']['name']
    rels = data['data']['relationships']

    # Get list of mangas
    mangas_id = []
    for rel in rels:
        _id = rel['id']
        _type = rel['type']
        if _type == "manga":
            manga = _fetch_manga(_id, "en", fetch_all_chapters=False, fetch_relationships=False)
            log.info("Found \"%s\" manga from \"%s\" list" % (manga.title, name))
            mangas_id.append(_id)

    for manga_id in mangas_id:
        download(
            manga_id,
            folder,
            replace,
            compressed_image,
            cover=cover,
            save_as=save_as,
            language=language
        )