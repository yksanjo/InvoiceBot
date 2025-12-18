# InvoiceBot 💰

> **Invoice Reminder Bot** - Automated follow-up bot for unpaid invoices. Integrates with Stripe and PayPal to track unpaid invoices and send reminder emails.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Status: Active](https://img.shields.io/badge/status-active-success.svg)](https://github.com/yksanjo/InvoiceBot)
[![GitHub stars](https://img.shields.io/github/stars/yksanjo/InvoiceBot?style=social)](https://github.com/yksanjo/InvoiceBot)

**InvoiceBot** automates the tedious task of following up on unpaid invoices. Set it and forget it - the bot will send friendly reminders at customizable intervals, helping you get paid faster.

## Features

- 💰 Stripe invoice tracking
- 💳 PayPal payment tracking
- 📧 Automated reminder emails
- ⏰ Customizable reminder schedule
- 📊 Payment analytics
- 🔔 Multi-channel notifications

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file:

```env
# Stripe Configuration
STRIPE_SECRET_KEY=sk_live_your_key
STRIPE_WEBHOOK_SECRET=whsec_your_secret

# PayPal Configuration (optional)
PAYPAL_CLIENT_ID=your_client_id
PAYPAL_CLIENT_SECRET=your_client_secret

# Email Configuration
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password

# Reminder Settings
REMINDER_DAYS=7,14,21  # Days after due date to send reminders
MAX_REMINDERS=3
```

## Usage

### Start Monitoring

```bash
python reminder_bot.py
```

### Check Invoices Once

```bash
python reminder_bot.py --check-once
```

### Send Manual Reminder

```bash
python reminder_bot.py --remind invoice_id
```

### View Unpaid Invoices

```bash
python reminder_bot.py --list-unpaid
```

## Reminder Schedule

Default reminder schedule:
- 7 days after due date: First reminder
- 14 days after due date: Second reminder
- 21 days after due date: Final reminder

## License

MIT License


