$(document).ready(function () {

	$('.scroll').click(function (e) {

		e.preventDefault();

		$('body,html').animate({

			scrollTop: $(this.hash).offset().top

		}, 2000)
	});

	const sr = ScrollReveal({
		duration: 1000,
		reset: true
	});

	// Scroll reveal section
	sr.reveal('.heading', {
	});
	sr.reveal('.jumbo1', {
		delay: 500
	});
	sr.reveal('.about', {
	});
	sr.reveal('.languages', {
	});
	sr.reveal('.purpose', {
	});
	sr.reveal('.previousWork', {
	});
	sr.reveal('.jobs', {
	});
	sr.reveal('.heroimage3', {
	});
	sr.reveal('.testimony', {
	});
	sr.reveal('.why', {
	});
	sr.reveal('.services', {
	});
	sr.reveal('.form', {
	});
	sr.reveal('footer', {
	});
});