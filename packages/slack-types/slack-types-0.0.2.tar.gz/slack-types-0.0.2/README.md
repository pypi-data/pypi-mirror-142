# Slack API types

See:
- https://pypi.org/project/slack-types

This npm package is a collection of Python and TypeScript type definition of Slack APIs.

Currently, the package support the following APIs.

* API Methods (web-api)
* Events API (events-api)
* Real Time Messaging API (rtm-api)
* Incoming payloads from Slack Platform (app-backend)
  * Dialogs (dialog_submission, cancellation, suggestion)
  * Interactive Messages (interactive_message, block_action)
  * Message Actions (message_action)
  * Slash Commands

## How to use

For Python:
```python
from typing import Callable

# Requirement: install aiohttp
from slack_bolt.async_app import AsyncApp
from slack_sdk.web.async_client import AsyncWebClient
from slack_types.events_api.app_mention_payload import Event as AppMentionEvent

app = AsyncApp()

@app.event("app_mention")
async def handle_mentions(event: dict[str, str], client: AsyncWebClient, say: Callable):  # async function
    slack_mention = AppMentionEvent.from_dict(event)
    api_response = await client.reactions_add(
        channel=slack_mention.channel,
        timestamp=slack_mention.ts,
        name="eyes",
    )
    await say("What's up?")

if __name__ == "__main__":
    app.start(3000)
```

For TypeScript:
```typescript
import * as express from 'express';
import { Express, Request, Response } from 'express';

import * as Slack from '@slack/web-api';
import * as WebApi from 'seratch-slack-types/web-api';
import * as EventsApi from 'seratch-slack-types/events-api';

export const slackApi = new Slack.WebClient(process.env.SLACK_API_TOKEN);

export const app: Express = express();

app.post('/events', function (req: Request, res: Response) {
  const body = JSON.parse(req.body); // still "any" here

  if (body.type === 'url_verification') {
    // url verification
    res.status(200).send(body.event.challenge);

  } else if (body.type === 'event_callback' && body.event.type === 'message') { // still "any" here
    const payload = body as EventsApi.MessagePayload;
    // `payload.event.text` here is typesafe
    slackApi.api.test({ text: payload.event.text })
      .then((response: WebApi.ApiTestResponse) => { // `response` is typesafe
        if (response.ok) {
         // do something here
        } else {
         // do something here
        }
      }).catch(reason => {
        // do something here
      });
  } else {
    // do something here
  }
  res.status(200).json({ message: 'thanks!' });
});
```

## How are the types generated

These types are generated from jSlack library's type definitions in Java + actual JSON responses fetched by running jSlack's unit tests. If you're interested in the details, take a look at [jSlack](https://github.com/seratch/jslack).

The coverage may not be 100% yet. A portion of the properties may be incorrect. If you find missing properties or something wrong, let us know here: https://github.com/seratch/seratch-slack-types/issues

To re-generate:

```bash
$ npm install
$ npm run build
```

## License

The MIT License
