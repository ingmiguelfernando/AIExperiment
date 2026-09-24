# Product — TakaheConnect

## What it is

TakaheConnect is Takahe Air's business-to-business booking API. It gives travel agencies, corporate travel managers and tour operators direct access to Takahe Air inventory without going through a global distribution system.

The platform began life as Takahe Air's internal booking engine, built during the 2020 border-closure shutdown when the fleet was grounded. It was opened to third parties in 2024.

## Why it exists

Global distribution systems charge a fee per booking segment, typically between NZD 4 and NZD 9. For a regional carrier with an average fare of NZD 142, that is a meaningful margin loss. TakaheConnect lets partners book directly at zero distribution cost to Takahe Air, and the airline shares part of that saving back as commission.

## How it works

TakaheConnect is a REST API with four core endpoints:

- `/search` — availability and pricing across the network
- `/book` — create a booking and hold it for 20 minutes
- `/ticket` — confirm and issue against a payment method
- `/manage` — change, cancel or transfer an existing booking

Authentication uses OAuth 2.0 client credentials. Rate limits are 100 requests per second per partner, raised on request.

## Commercial terms

| Partner tier | Annual segment volume | Commission |
|---|---|---|
| Standard | Under 5,000 | 3 percent |
| Preferred | 5,000 to 25,000 | 5 percent |
| Strategic | Over 25,000 | 7 percent plus dedicated support |

There is no licence fee and no minimum volume commitment. Partners are billed nothing for API access.

## Service levels

TakaheConnect committed availability is 99.9 percent measured monthly. Actual availability in FY2026 was 99.95 percent. Scheduled maintenance windows are Sunday 02:00 to 04:00 NZST and are excluded from the calculation.

Partners on the Strategic tier receive a named technical contact and a four-hour response commitment for production incidents.

## Performance

TakaheConnect generated NZD 14.2 million in FY2026 and carries 28 percent of Takahe Air's total bookings. Tomas Vella, who made the original decision to build the platform in-house, describes it as the clearest return on the airline's engineering investment.
