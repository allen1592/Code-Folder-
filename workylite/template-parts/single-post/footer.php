<?php
/**
 * Template part for displaying posts
 *
 * @link https://developer.wordpress.org/themes/basics/template-hierarchy/
 *
 * @package Worky
 */

?>

<footer class="entry-footer">
	<div class="entry-meta"><?php
		worky_post_tags ( array(
			'prefix'    => __( 'Tags:', 'worky' ),
			'delimiter' => ''
		) );
	?></div>
</footer><!-- .entry-footer -->