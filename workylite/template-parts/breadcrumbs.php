<?php
/**
 * Template part for breadcrumbs.
 *
 * @link https://codex.wordpress.org/Template_Hierarchy
 *
 * @package Worky
 */

$breadcrumbs_visibillity = worky_theme()->customizer->get_value( 'breadcrumbs_visibillity' );

/**
 * [$breadcrumbs_visibillity description]
 * @var [type]
 */
$breadcrumbs_visibillity = apply_filters( 'worky-theme/breadcrumbs/breadcrumbs-visibillity', $breadcrumbs_visibillity );

if ( ! $breadcrumbs_visibillity ) {
	return;
}

$breadcrumbs_front_visibillity = worky_theme()->customizer->get_value( 'breadcrumbs_front_visibillity' );

if ( !$breadcrumbs_front_visibillity && is_front_page() ) {
	return;
}

do_action( 'worky-theme/breadcrumbs/breadcrumbs-before-render' );

?><div <?php echo worky_get_container_classes( 'site-breadcrumbs' ); ?>>
	<div <?php worky_breadcrumbs_class(); ?>>
		<?php do_action( 'worky-theme/breadcrumbs/before' ); ?>
		<?php do_action( 'cx_breadcrumbs/render' ); ?>
		<?php do_action( 'worky-theme/breadcrumbs/after' ); ?>
	</div>
</div><?php

do_action( 'worky-theme/breadcrumbs/breadcrumbs-after-render' );
