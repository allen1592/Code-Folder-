<?php
/**
 * Template part for default Header layout.
 *
 * @link https://codex.wordpress.org/Template_Hierarchy
 *
 * @package Worky
 */
?>

<?php get_template_part( 'template-parts/top-panel' ); ?>

<div <?php worky_header_class(); ?>>
	<?php do_action( 'worky-theme/header/before' ); ?>
	<div class="space-between-content">
		<div <?php worky_site_branding_class(); ?>>
			<?php worky_header_logo(); ?>
		</div>
		<?php worky_main_menu(); ?>
	</div>
	<?php do_action( 'worky-theme/header/after' ); ?>
</div>


