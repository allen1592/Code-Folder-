<?php
/**
 * Template part for displaying default posts
 *
 * @link https://developer.wordpress.org/themes/basics/template-hierarchy/
 *
 * @package Worky
 */

?>

<article id="post-<?php the_ID(); ?>" <?php post_class('post-default'); ?>>

	<header class="entry-header">
		<h3 class="entry-title"><?php 
			worky_sticky_label();
			the_title( '<a href="' . esc_url( get_permalink() ) . '" rel="bookmark">', '</a>' );
		?></h3>
		<div class="entry-meta">
			<?php
				worky_posted_by();
				worky_posted_in( array(
					'prefix' => __( 'In', 'worky' ),
				) );
				worky_posted_on( array(
					'prefix' => __( 'Posted', 'worky' )
				) );
			?>
		</div><!-- .entry-meta -->
	</header><!-- .entry-header -->

	<?php worky_post_thumbnail( 'worky-thumb-l' ); ?>

	<?php worky_post_excerpt(); ?>

	<footer class="entry-footer">
		<div class="entry-meta">
			<?php
				worky_post_tags( array(
					'prefix' => __( 'Tags:', 'worky' )
				) );
			?>
			<div><?php
				worky_post_comments( array(
					'prefix' => '<i class="fa fa-comment" aria-hidden="true"></i>',
					'class'  => 'comments-button'
				) );
				worky_post_link();
			?></div>
		</div>
		<?php worky_edit_link(); ?>
	</footer><!-- .entry-footer -->
	
</article><!-- #post-<?php the_ID(); ?> -->
