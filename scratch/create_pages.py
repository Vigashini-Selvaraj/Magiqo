import os

with open('privacy-policy.html', 'r', encoding='utf-8') as f:
    template = f.read()

def generate_page(filename, title, h1_pink, h1_blue, desc, sections):
    # Replace title
    html = template.replace('<title>Privacy Policy | Magiqo</title>', f'<title>{title}</title>')
    
    # Replace hero
    html = html.replace('<span class="text-pink">Privacy</span> <span class="text-blue">Policy</span>', f'<span class="text-pink">{h1_pink}</span> <span class="text-blue">{h1_blue}</span>')
    html = html.replace('<p>Your privacy is important to us. Learn how we collect, use, and protect your personal information.</p>', f'<p>{desc}</p>')
    
    # Extract content section
    start_tag = '<div class="content-container">'
    end_tag = '<p style="margin-top: 40px; font-style: italic; color: #888;">Last updated:'
    
    start_idx = html.find(start_tag) + len(start_tag)
    end_idx = html.find(end_tag)
    
    # Build new content
    content_html = "\n"
    for heading, text in sections:
        content_html += f"        <h2>{heading}</h2>\n"
        content_html += f"        <p>{text}</p>\n\n"
    
    new_html = html[:start_idx] + content_html + "        " + html[end_idx:]
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_html)


# Pricing Policy
generate_page(
    'pricing-policy.html',
    'Pricing Policy | Magiqo',
    'Pricing', 'Policy',
    'Learn about our transparent pricing, booking fees, and refund policies for all magical entertainment.',
    [
        ("1. Transparent Pricing", "All entertainer packages on Magiqo are priced upfront. What you see is what you pay. There are no hidden fees or surprise charges after your booking is confirmed."),
        ("2. Booking Fees & Deposits", "A small service fee is applied to each booking to maintain the Magiqo platform and provide 24/7 customer support. Some entertainers may require a non-refundable deposit to secure your date, which will be clearly stated during checkout."),
        ("3. Cancellations & Refunds", "If you cancel a booking at least 7 days before the event, you will receive a full refund (minus any non-refundable deposit). Cancellations made within 7 days of the event may be subject to a 50% cancellation fee."),
        ("4. Overtime Charges", "If your event runs longer than the booked time, overtime charges may apply at the entertainer's standard hourly rate, billed in 30-minute increments.")
    ]
)

# Terms of Service
generate_page(
    'terms.html',
    'Terms of Service | Magiqo',
    'Terms', 'of Service',
    'Please read these terms carefully before using the Magiqo platform to book event entertainment.',
    [
        ("1. Acceptance of Terms", "By accessing and using Magiqo, you accept and agree to be bound by the terms and provision of this agreement."),
        ("2. User Responsibilities", "You must be at least 18 years old to create an account and book entertainers. You agree to provide accurate, current, and complete information during the booking process."),
        ("3. Entertainer Conduct", "Magiqo acts as a marketplace. While we vet our entertainers, we are not directly responsible for their conduct. However, we take user feedback seriously and reserve the right to remove entertainers who violate our community standards."),
        ("4. Limitation of Liability", "Magiqo shall not be liable for any direct, indirect, incidental, special, or consequential damages resulting from the use or inability to use our services or the performance of any booked entertainer.")
    ]
)

# Help Center
generate_page(
    'help.html',
    'Help Center | Magiqo',
    'Help', 'Center',
    'Need assistance? Find answers to common questions and learn how to get the most out of Magiqo.',
    [
        ("1. How to Book an Entertainer", "Browse our categories, select an entertainer, choose a package, and click 'Book Now'. You'll be prompted to enter your event details and secure the booking with a payment."),
        ("2. Managing Your Bookings", "You can view, modify, or cancel your upcoming events by logging into your account and navigating to the 'My Bookings' tab in your user dashboard."),
        ("3. Payment Issues", "If your payment is declined, please ensure your card details are correct or try an alternative payment method. For billing inquiries, contact our support team."),
        ("4. Contact Support", "If you still need help, our dedicated support team is available 24/7. Please visit our Contact page to send us a message, or email us directly at support@magiqo.com.")
    ]
)

print("Created pricing-policy.html, terms.html, and help.html")
