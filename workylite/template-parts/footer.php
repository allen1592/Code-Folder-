<?php
/**
 * The template for displaying the default footer layout.
 *
 * @package Worky
 */
?>

<?php do_action( 'worky-theme/widget-area/render', 'footer-area' ); ?>

<div <?php worky_footer_class(); ?>>
	<div class="space-between-content"><?php
		worky_footer_copyright();
		worky_social_list( 'footer' );
	?></div>
</div><!-- .container -->
