<?php
/**
 * The header for our theme.
 *
 * This is the template that displays all of the <head> section and everything up until <div id="content">
 *
 * @link https://developer.wordpress.org/themes/basics/template-files/#template-partials
 *
 * @package Worky
 */

?><!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
<meta charset="<?php bloginfo( 'charset' ); ?>">
<link rel="profile" href="http://gmpg.org/xfn/11">
<link rel="pingback" href="<?php bloginfo( 'pingback_url' ); ?>">

<?php wp_head(); ?>
</head>

<body <?php body_class(); ?>>
<?php do_action( 'worky-theme/site/page-start' ); ?>
<?php worky_get_page_preloader(); ?>
<div id="page" class="site">
	<a class="skip-link screen-reader-text" href="#content"><?php esc_html_e( 'Skip to content', 'worky' ); ?></a>
	<header id="masthead" <?php echo worky_get_container_classes( 'site-header' ); ?>>
		<a href="https://www.templatemonster.com/wordpress-themes/worky-architectural-bureau-multipurpose-modern-elementor-wordpress-theme-76333.html" class="monst2-link">
			<img class="big-monst2" src=<?php echo get_template_directory_uri()."/assets/banners/monstroid2-big.png"; ?> alt="monstroid2">
			<img class="small-monst2" src=<?php echo get_template_directory_uri()."/assets/banners/monstroid2-small.png"; ?> alt="monstroid2">
		</a>
        <?php worky_top_panel_banner(); ?>
		<?php get_template_part( 'template-parts/header', 'header' ); ?>
	</header><!-- #masthead -->
	<?php get_template_part( 'template-parts/breadcrumbs' ); ?>
	<div id="content" <?php echo worky_get_container_classes( 'site-content' ); ?>>
