## Overview

Eyes of an Addict is a Flask-based web application for a recovery community platform. The site serves as a digital presence for D. Bailey, a Certified Peer Recovery Support Specialist, providing resources, products, and community support for people in early recovery. The application features a simple informational website with contact functionality, product showcases, and community information.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Template Engine**: Jinja2 with Flask's built-in templating
- **CSS Framework**: Pico CSS for minimal, semantic styling
- **Icons**: Feather Icons for consistent iconography
- **Layout Pattern**: Base template inheritance for consistent navigation and structure
- **Responsive Design**: Mobile-first approach with CSS Grid for layouts

### Backend Architecture
- **Framework**: Flask (Python microframework)
- **Application Structure**: Simple modular design with separate files for routes, forms, and main application
- **Form Handling**: Flask-WTF with WTForms for contact form validation and CSRF protection
- **Error Handling**: Custom error handlers for 404 and 500 errors
- **Session Management**: Flask sessions with configurable secret key
- **Logging**: Python's built-in logging module for debugging and contact form submissions

### Data Storage Solutions
- **Current State**: No database implementation - contact forms are logged only
- **Form Data**: Contact submissions are currently logged to console/files
- **Static Assets**: File-based storage for CSS, images, and other static content
- **Session Storage**: Flask's default session storage (cookie-based)

### Authentication and Authorization
- **Current Implementation**: No authentication system implemented
- **Security**: CSRF protection through Flask-WTF for forms
- **Session Security**: Configurable session secret key through environment variables

## External Dependencies

### Third-party Services
- **CDN Resources**: 
  - Pico CSS framework (cdn.jsdelivr.net)
  - Feather Icons (cdn.jsdelivr.net)

### Python Libraries
- **Flask**: Core web framework
- **Flask-WTF**: Form handling and CSRF protection
- **WTForms**: Form validation and rendering

### Future Integrations
- **Email Service**: Will need email integration for contact form functionality
- **E-commerce Platform**: Product links suggest future integration with external shop
- **Social Media**: Links prepared for Facebook, Instagram, TikTok integration
- **Payment Processing**: Required for digital product sales and coaching services

### Development Dependencies
- **Environment**: Designed for development with debug mode enabled
- **Deployment**: Configured for cloud deployment (0.0.0.0 host binding)
- **Asset Management**: Static file serving through Flask's built-in capabilities
