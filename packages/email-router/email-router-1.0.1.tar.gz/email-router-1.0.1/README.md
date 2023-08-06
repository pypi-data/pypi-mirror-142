# Email Router

A straightforward and efficient inbound email router. This library allows you to route emails depending on its contents to different destinations with a concise YAML configuration. Combine "conditions" and "handlers" together to create "routes" that determine where to send each email.

This library is best used alongside SendGrid's [Inbound Parse](https://docs.sendgrid.com/for-developers/parsing-email/setting-up-the-inbound-parse-webhook) or a variation of it and is a more powerful version of Mailgun's [inbound routing](https://www.mailgun.com/inbound-routing/).

## Installation
```sh
$ python3 -m pip install email-router
```
