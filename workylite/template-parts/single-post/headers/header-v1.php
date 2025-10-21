<?php
/**
 * Template part for displaying posts
 *
 * @link https://developer.wordpress.org/themes/basics/template-hierarchy/
 *
 * @package Worky
 */

?>

<header class="entry-header">
	<?php the_title( '<h1 class="entry-title h2-style">', '</h1>' ); ?>
	<div class="entry-meta">
		<?php
			worky_posted_by();
			worky_posted_in( array(
				'prefix'  => __( 'In', 'worky' ),
			) );
			worky_posted_on( array(
				'prefix'  => __( 'Posted', 'worky' ),
			) );
			worky_post_comments( array(
				'postfix' => __( 'Comment(s)', 'worky' ),
			) );
		?>
	</div><!-- .entry-meta -->
</header><!-- .entry-header -->

<?php worky_post_thumbnail( 'worky-thumb-l', array( 'link' => false ) ); ?>