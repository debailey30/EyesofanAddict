from flask import render_template, request, flash, redirect, url_for
from app import app
from forms import ContactForm
import logging

@app.route('/')
def index():
    """Main homepage with hero section and overview"""
    return render_template('index.html')

@app.route('/products')
def products():
    """Product showcase page for digital and POD items"""
    return render_template('products.html')

@app.route('/faq')
def faq():
    """FAQ page with common questions"""
    return render_template('faq.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page with form for community inquiries"""
    form = ContactForm()
    
    if form.validate_on_submit():
        # Log the contact form submission (in production, you'd send an email or save to database)
        logging.info(f"Contact form submitted: {form.name.data} ({form.email.data}) - {form.subject.data}")
        
        flash(f"Thank you {form.name.data}! Your message has been received. We'll get back to you soon.", 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return render_template('base.html', error_message="Page not found"), 404

@app.errorhandler(500)
def internal_error(e):
    """Handle 500 errors"""
    return render_template('base.html', error_message="Internal server error"), 500