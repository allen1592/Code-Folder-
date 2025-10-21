<?php
/**
 * Sidebars configuration.
 *
 * @package Worky
 */

add_action( 'after_setup_theme', 'worky_register_sidebars', 5 );
function worky_register_sidebars() {

	worky_widget_area()->widgets_settings = apply_filters( 'worky-theme/widget_area/default_settings', array(
		'sidebar' => array(
			'name'           => esc_html__( 'Sidebar', 'worky' ),
			'description'    => '',
			'before_widget'  => '<aside id="%1$s" class="widget %2$s">',
			'after_widget'   => '</aside>',
			'before_title'   => '<h4 class="widget-title">',
			'after_title'    => '</h4>',
			'before_wrapper' => '<div id="%1$s" %2$s role="complementary">',
			'after_wrapper'  => '</div>',
			'is_global'      => true,
		),
	) );
}
