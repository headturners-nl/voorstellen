<?php
/**
 * Headturners thema.
 */

function ht_pages() {
  return array(
    'home' => array( 'title' => "Home", 'doc_title' => "Headturners | Websites voor ondernemers, door een ondernemer", 'desc' => "Websites, advertenties, social media en branding voor ondernemers. Eerst gratis een voorstel van je nieuwe homepage, daarna beslis je." ),
    'websites' => array( 'title' => "Websites", 'doc_title' => "Websites laten maken | Headturners", 'desc' => "Een website in je eigen huisstijl die klanten oplevert. Huren vanaf €59 per maand of kopen vanaf €695. Eerst gratis een voorstel." ),
    'advertenties' => array( 'title' => "Advertenties", 'doc_title' => "Google Ads en Meta Ads | Headturners", 'desc' => "Google Ads en Meta Ads beheer voor ondernemers. Eerst een gesprek over je bedrijf, daarna campagnes die elke maand worden bijgestuurd." ),
    'social-en-blogs' => array( 'title' => "Social media en blogs", 'doc_title' => "Social media en blogs | Headturners", 'desc' => "Social media beheer voor Facebook en Instagram en blogs voor Google. In jouw stijl, vooraf door jou goedgekeurd." ),
    'branding' => array( 'title' => "Branding", 'doc_title' => "Branding: logo, huisstijl, visie en missie | Headturners", 'desc' => "Branding voor ondernemers: visie, missie, doelgroep, logo, kleuren, lettertypes en een stijlgids. Vanaf €795." ),
    'voorbeelden' => array( 'title' => "Voorbeelden", 'doc_title' => "Voorbeelden van websites | Headturners", 'desc' => "Bekijk het verschil tussen de oude en nieuwe websites van ondernemers die met Headturners werken." ),
    'over' => array( 'title' => "Over mij", 'doc_title' => "Over Mar | Headturners", 'desc' => "Mar is ondernemer met een eigen praktijk en bouwt websites, advertenties en content voor andere ondernemers." ),
    'contact' => array( 'title' => "Contact", 'doc_title' => "Gratis voorstel aanvragen | Headturners", 'desc' => "Vraag gratis een voorstel aan voor je nieuwe website. Geen kosten, geen verplichtingen." ),
    'rebranding-sami' => array( 'title' => "Rebranding Sami's Acupunctuur", 'doc_title' => "De rebranding van Sami's Acupunctuur | Headturners", 'desc' => "Loop zelf het branding traject van Sami's Acupunctuur door: kijken, kiezen, voelen, schrappen en live." ),
    'privacyverklaring' => array( 'title' => "Privacyverklaring", 'doc_title' => "Privacyverklaring | Headturners", 'desc' => "Hoe Headturners omgaat met je persoonsgegevens." ),
    'cookieverklaring' => array( 'title' => "Cookieverklaring", 'doc_title' => "Cookieverklaring | Headturners", 'desc' => "Welke cookies headturners.nl gebruikt." ),
    'algemene-voorwaarden' => array( 'title' => "Algemene voorwaarden", 'doc_title' => "Algemene voorwaarden | Headturners", 'desc' => "De algemene voorwaarden van Headturners." )
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
    echo '<meta name="description" content="' . esc_attr( $p[ $s ]['desc'] ) . '">' . "\n";
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
  $sent = wp_mail( $to, $subject, implode( "
", $lines ), $headers );
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
      echo '<div class="notice notice-success"><p>Alle pagina\'s zijn teruggezet naar de versie uit het thema.</p></div>';
    }
    echo '<div class="wrap"><h1>Headturners</h1><p>Zet alle pagina\'s terug naar de versie uit het thema. Eigen wijzigingen in de pagina\'s gaan dan verloren.</p><form method="post">';
    wp_nonce_field( 'ht_reset' );
    echo '<p><button class="button button-primary" name="ht_reset" value="1">Pagina\'s terugzetten</button></p></form></div>';
  } );
} );
