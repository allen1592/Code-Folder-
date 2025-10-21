<?php
/**
 * Menus configuration.
 *
 * @package Worky
 */

add_action( 'after_setup_theme', 'worky_register_menus', 5 );
function worky_register_menus() {

	register_nav_menus( array(
		'main'   => esc_html__( 'Main', 'worky' ),
		'footer' => esc_html__( 'Footer', 'worky' ),
		'social' => esc_html__( 'Social', 'worky' ),
	) );
}
