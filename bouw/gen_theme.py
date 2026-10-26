"""Turn the static Headturners site into a WordPress theme (headturners/)."""
import os, re, shutil, json

BASE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(BASE, '..', 'site')
OUT = os.path.join(BASE, '..', 'theme', 'headturners')

PAGES = [  # file, slug, wp title
    ('index.html', 'home', 'Home'),
    ('websites.html', 'websites', 'Websites'),
    ('advertenties.html', 'advertenties', 'Advertenties'),
    ('social-en-blogs.html', 'social-en-blogs', 'Social media en blogs'),
    ('branding.html', 'branding', 'Branding'),
    ('voorbeelden.html', 'voorbeelden', 'Voorbeelden'),
    ('over.html', 'over', 'Over mij'),
    ('contact.html', 'contact', 'Contact'),
    ('rebranding-sami.html', 'rebranding-sami', "Rebranding Sami's Acupunctuur"),
    ('privacyverklaring.html', 'privacyverklaring', 'Privacyverklaring'),
    ('cookieverklaring.html', 'cookieverklaring', 'Cookieverklaring'),
    ('algemene-voorwaarden.html', 'algemene-voorwaarden', 'Algemene voorwaarden'),
]
SLUG = {f: s for f, s, _ in PAGES}


def links(html):
    def rep(m):
        attr, file, rest = m.group(1), m.group(2), m.group(3) or ''
        slug = SLUG.get(file)
        if slug is None:
            return m.group(0)
        path = '/' if slug == 'home' else f'/{slug}/'
        return f'{attr}="{{{{H}}}}{path}{rest}"'
    html = re.sub(r'(href)="([a-z\-]+\.html)([?#][^"]*)?"', rep, html)
    html = re.sub(r'(src|href)="(klanten/|assets/|logo-mark\.svg)', lambda m: f'{m.group(1)}="{{{{T}}}}/{m.group(2)}', html)
    return html


def part(html, start, end):
    i = html.index(start); j = html.index(end, i) + len(end)
    return html[i:j]


if os.path.exists(OUT):
    shutil.rmtree(OUT)
os.makedirs(os.path.join(OUT, 'content'))
for d in ('assets', 'klanten'):
    shutil.copytree(os.path.join(SITE, d), os.path.join(OUT, d))
shutil.copy(os.path.join(SITE, 'logo-mark.svg'), OUT)
shutil.copy(os.path.join(SITE, 'klanten.json'), OUT)

meta = {}
for f, slug, title in PAGES:
    html = open(os.path.join(SITE, f), encoding='utf-8').read()
    doc_title = re.search(r'<title>(.*?)</title>', html, re.S).group(1)
    desc = re.search(r'<meta name="description" content="(.*?)">', html, re.S).group(1)
    meta[slug] = {'title': title, 'doc_title': doc_title, 'desc': desc}
    body = html[html.index('<main id="top">') + len('<main id="top">'):html.index('</main>')]
    body = re.sub(r'<link rel="stylesheet" href="assets/case\.css">\s*', '', body)
    body = re.sub(r'<script src="assets/case\.js" defer></script>\s*', '', body)
    body = links(body).strip()
    open(os.path.join(OUT, 'content', slug + '.html'), 'w', encoding='utf-8').write(
        '<!-- wp:html -->\n' + body + '\n<!-- /wp:html -->\n')

home = open(os.path.join(SITE, 'index.html'), encoding='utf-8').read()
header = links(part(home, '<header class="site">', '</header>'))
footer = links(part(home, '<footer class="site">', '</footer>')) + '\n' + links(part(home, '<div class="mcta">', '</div>'))
header = header.replace(' aria-current="page"', '')


def php(s):
    return s.replace('{{H}}', "<?php echo esc_url( home_url() ); ?>").replace('{{T}}', "<?php echo esc_url( get_template_directory_uri() ); ?>")


open(os.path.join(OUT, 'header.php'), 'w', encoding='utf-8').write(f'''<!doctype html>
<html <?php language_attributes(); ?>>
<head>
<meta charset="<?php bloginfo( 'charset' ); ?>">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="<?php echo esc_url( get_template_directory_uri() ); ?>/logo-mark.svg" type="image/svg+xml">
<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>
{php(header)}
<main id="top">
''')
open(os.path.join(OUT, 'footer.php'), 'w', encoding='utf-8').write(f'''</main>
{php(footer)}
<?php wp_footer(); ?>
</body>
</html>
''')

loop = '''<?php get_header(); ?>
<?php while ( have_posts() ) : the_post(); the_content(); endwhile; ?>
<?php get_footer(); ?>
'''
for name in ('index.php', 'page.php', 'front-page.php'):
    open(os.path.join(OUT, name), 'w').write(loop)

open(os.path.join(OUT, 'style.css'), 'w').write('''/*
Theme Name: Headturners
Theme URI: https://headturners.nl
Author: Headturners
Description: Thema voor Headturners. Bij activeren worden alle pagina's, het menu en de homepage automatisch aangemaakt.
Version: 1.1
Requires at least: 6.0
Requires PHP: 7.4
Text Domain: headturners
*/
''')

pages_php = ',\n'.join(
    f"    '{s}' => array( 'title' => {json.dumps(m['title'], ensure_ascii=False)}, 'doc_title' => {json.dumps(m['doc_title'], ensure_ascii=False)}, 'desc' => {json.dumps(m['desc'], ensure_ascii=False)} )"
    for s, m in meta.items()).replace('$', '\\$')

open(os.path.join(OUT, 'functions.php'), 'w', encoding='utf-8').write('''<?php
/**
 * Headturners thema.
 */

function ht_pages() {
  return array(
''' + pages_php + '''
  );
}

add_action( 'after_setup_theme', function () {
  add_theme_support( 'title-tag' );
} );

/* Styles and scripts */
add_action( 'wp_enqueue_scripts', function () {
  $t = get_template_directory_uri();
  $v = wp_get_theme()->get( 'Version' );
  wp_enqueue_style( 'ht-fonts', $t . '/assets/fonts.css', array(), $v );
  wp_enqueue_style( 'ht-style', $t . '/assets/style.css', array(), $v );
  wp_enqueue_script( 'ht-main', $t . '/assets/main.js', array(), $v, true );
  wp_add_inline_script( 'ht-main', 'window.HT=' . wp_json_encode( array( 'base' => $t . '/', 'home' => home_url( '/' ), 'api' => rest_url( 'headturners/v1/aanvraag' ) ) ) . ';', 'before' );
  if ( is_page( 'rebranding-sami' ) ) {
    wp_enqueue_style( 'ht-case', $t . '/assets/case.css', array( 'ht-style' ), $v );
    wp_enqueue_script( 'ht-case', $t . '/assets/case.js', array(), $v, true );
  }
  /* Block styles are not used by this theme */
  wp_dequeue_style( 'wp-block-library' );
  wp_dequeue_style( 'global-styles' );
  wp_dequeue_style( 'classic-theme-styles' );
}, 20 );

/* Placeholders in page content: {{H}} = site address, {{T}} = theme folder */
function ht_placeholders( $html ) {
  return str_replace(
    array( '{{H}}', '{{T}}' ),
    array( untrailingslashit( home_url() ), get_template_directory_uri() ),
    $html
  );
}
add_filter( 'the_content', 'ht_placeholders', 99 );
remove_filter( 'the_content', 'wpautop' );

/* Page titles and descriptions for Google */
add_filter( 'pre_get_document_title', function ( $title ) {
  if ( is_front_page() ) { $s = 'home'; } elseif ( is_page() ) { $s = get_post_field( 'post_name', get_queried_object_id() ); } else { return $title; }
  $p = ht_pages();
  return isset( $p[ $s ] ) ? $p[ $s ]['doc_title'] : $title;
} );
add_action( 'wp_head', function () {
  if ( is_front_page() ) { $s = 'home'; } elseif ( is_page() ) { $s = get_post_field( 'post_name', get_queried_object_id() ); } else { return; }
  $p = ht_pages();
  if ( isset( $p[ $s ] ) ) {
    echo '<meta name="description" content="' . esc_attr( $p[ $s ]['desc'] ) . '">' . "\\n";
  }
}, 1 );

/* Contact page has its own form, so no sticky button there */
add_filter( 'body_class', function ( $c ) {
  if ( is_page( 'contact' ) ) { $c[] = 'no-mcta'; }
  return $c;
} );

/* Create all pages once, when the theme is activated */
function ht_install_pages( $force = false ) {
  $ver = wp_get_theme( get_template() )->get( 'Version' );
  if ( ! $force && get_option( 'ht_pages_installed' ) === $ver ) { return; }
  kses_remove_filters();
  $dir = get_template_directory() . '/content/';
  $front = 0;
  foreach ( ht_pages() as $slug => $p ) {
    $html = file_get_contents( $dir . $slug . '.html' );
    $existing = get_page_by_path( $slug, OBJECT, 'page' );
    $data = array(
      'post_title'   => $p['title'],
      'post_name'    => $slug,
      'post_content' => $html,
      'post_status'  => 'publish',
      'post_type'    => 'page',
    );
    if ( $existing ) {
      if ( ! $force ) { if ( 'home' === $slug ) { $front = $existing->ID; } continue; }
      $data['ID'] = $existing->ID;
      $id = wp_update_post( wp_slash( $data ) );
    } else {
      $id = wp_insert_post( wp_slash( $data ) );
    }
    if ( 'home' === $slug ) { $front = $id; }
  }
  kses_init_filters();
  if ( $front ) {
    update_option( 'show_on_front', 'page' );
    update_option( 'page_on_front', $front );
  }
  if ( '' === get_option( 'permalink_structure' ) ) {
    update_option( 'permalink_structure', '/%postname%/' );
  }
  flush_rewrite_rules();
  update_option( 'ht_pages_installed', $ver );
}
add_action( 'after_switch_theme', function () { ht_install_pages( false ); } );
/* After a theme update: add pages that are new in this version */
add_action( 'admin_init', function () { if ( current_user_can( 'manage_options' ) ) { ht_install_pages( false ); } } );

/* Contact form: sends the request to info@headturners.nl */
add_action( 'rest_api_init', function () {
  register_rest_route( 'headturners/v1', '/aanvraag', array(
    'methods'             => 'POST',
    'permission_callback' => '__return_true',
    'callback'            => 'ht_aanvraag',
  ) );
} );
function ht_aanvraag( WP_REST_Request $req ) {
  $d = $req->get_json_params();
  if ( ! is_array( $d ) ) { $d = array(); }
  if ( ! empty( $d['website_url'] ) ) { return array( 'ok' => true ); } /* spam trap */
  $ip  = isset( $_SERVER['REMOTE_ADDR'] ) ? $_SERVER['REMOTE_ADDR'] : '';
  $key = 'ht_rl_' . md5( $ip );
  $n   = (int) get_transient( $key );
  if ( $n >= 5 ) {
    return new WP_REST_Response( array( 'ok' => false, 'message' => 'Je hebt al een paar aanvragen gestuurd. Mail me gerust direct via info@headturners.nl.' ), 429 );
  }
  $f = function ( $k ) use ( $d ) { return isset( $d[ $k ] ) ? sanitize_text_field( wp_unslash( $d[ $k ] ) ) : ''; };
  $naam  = $f( 'naam' );
  $email = isset( $d['email'] ) ? sanitize_email( $d['email'] ) : '';
  if ( '' === $naam || ! is_email( $email ) ) {
    return new WP_REST_Response( array( 'ok' => false, 'message' => 'Vul je naam en een geldig mailadres in.' ), 400 );
  }
  $bericht = isset( $d['bericht'] ) ? sanitize_textarea_field( wp_unslash( $d['bericht'] ) ) : '';
  $lines = array(
    'Naam: ' . $naam,
    'Mail: ' . $email,
    'Bedrijf: ' . $f( 'bedrijf' ),
    'Telefoon: ' . $f( 'telefoon' ),
    'Huidige website of Instagram: ' . $f( 'site' ),
    'Interesse: ' . $f( 'dienst' ),
    '',
    $bericht,
    '',
    'Verstuurd via headturners.nl op ' . wp_date( 'j F Y H:i' ),
  );
  $to      = 'info@headturners.nl';
  $subject = 'Nieuwe aanvraag van ' . ( $f( 'bedrijf' ) ? $f( 'bedrijf' ) : $naam );
  $headers = array( 'From: Headturners website <info@headturners.nl>', 'Reply-To: ' . $naam . ' <' . $email . '>' );
  $sent = wp_mail( $to, $subject, implode( "\n", $lines ), $headers );
  set_transient( $key, $n + 1, HOUR_IN_SECONDS );
  if ( ! $sent ) {
    return new WP_REST_Response( array( 'ok' => false, 'message' => 'Versturen lukte niet. Mail je aanvraag naar info@headturners.nl.' ), 500 );
  }
  return array( 'ok' => true );
}

/* Tools > Headturners: reset pages to the theme version */
add_action( 'admin_menu', function () {
  add_management_page( 'Headturners', 'Headturners', 'manage_options', 'headturners', function () {
    if ( isset( $_POST['ht_reset'] ) && check_admin_referer( 'ht_reset' ) ) {
      ht_install_pages( true );
      echo '<div class="notice notice-success"><p>Alle pagina\\'s zijn teruggezet naar de versie uit het thema.</p></div>';
    }
    echo '<div class="wrap"><h1>Headturners</h1><p>Zet alle pagina\\'s terug naar de versie uit het thema. Eigen wijzigingen in de pagina\\'s gaan dan verloren.</p><form method="post">';
    wp_nonce_field( 'ht_reset' );
    echo '<p><button class="button button-primary" name="ht_reset" value="1">Pagina\\'s terugzetten</button></p></form></div>';
  } );
} );
''')

print('theme written to', os.path.abspath(OUT))
