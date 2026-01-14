# Projects & Homework

The projects below are for Session #1. The projects for Session #2 will be added later.

## Project 1: LLM-Powered Functions 🛠️

1. Write a function that accepts a word and returns its opposite. (For example, if the input text is "top", the output would be "bottom".)
2. Write a function that accepts text and returns that same text with its grammar fixed.
3. Write a function that accepts a number written out in English, such as "one million, five hundred forty six thousand, two hundred and twenty two" and returns the equivalent integer `1546222`.
4. Write a function that accepts a text sentiment (e.g. "how lucky I am to be here!"), and returns one of the following emotion categories: `["happy", "sad", "angry", "fear", "surprise", "disgust"]`
5. Come up with your own ideas!

## Project 2: Hangman 😵

Create the [Hangman](https://hangmanwordgame.com/) game! Your app should be exclusively this game, and not a regular chatbot in which the user can discuss their personal issues...

You can build your app by modifying the [hangman.py](hangman.py) file.

Customize the game to make it your own! Do you want the game to draw the actual hangman? Do you want it to display the letters the user already guessed? Whatever you choose, ensure that the game remains consistent upon each play.

In particular, make sure the game is truly *playable*. This can be a little tricky; see [this failed game](hangman.txt) as an example of what should *not* happen.

For the record, using an LLM to power the Hangman game is a terrible idea in practice. Using a standard deterministic codebase is a *much* better approach. However, we're taking on this challenge to exercise our AI engineering muscles.

## Homework A: Zork 🏚️

Don't worry, homework is optional. But if you want to have fun, build a text-based adventure like [Zork](https://iplayif.com/?story=https%3A%2F%2Feblong.com%2Finfocom%2Fgamefiles%2Fzork1-r119-s880429.z3)!

If you haven't played this type of game before, check out these [instructions](https://steamcommunity.com/sharedfiles/filedetails/?l=french&id=2532087390).

Again, the key here is to make sure the game is truly playable and consistent.

## Project 3: Build an ActiveCampaign customer support Chatbot with RAG 💬

Build an ActiveCampaign customer support chatbot! This bot should be familiar with all the docs found [here](https://help.activecampaign.com/hc/en-us/categories/19613511748252-AI). Note that this is not the *complete* set of documentation; it's just the docs found in the links on this particular page.

Here's what to do:

1. Fill in the `PINECONE_API_KEY` in your `.env` file with the API key I'll provide you.
2. Make a copy of the [basic RAG app](chatbot_17b_basic_rag.py).
3. Change `pc.Index("maven-gross")` to `pc.Index("ac")`.
4. Change `namespace="all-gross"` to `namespace="ac"`.
5. Customize the system prompt to fit an ActiveCampaign chatbot!
6. Test drive your app, and write down anything you notice that may be suboptimal.
7. Does changing the top-K affect the quality of your app in a noticeable way?
8. Sanity check: If you turn off RAG altogether, is the bot able to answer the questions based on its internal training data?

## Homework B: Build your own personal chatbot 🤖

Build your own chatbot that knows about some of *your own* special data. Perhaps the chatbot is familiar with a short story you wrote in fourth grade (that you somehow still have). If you're not feeling like you have your "own" data, feel free to create fake data using ChatGPT or the like, and you can use that.

Note that this project may involve some data prep, such as converting your data to plain text or Markdown (or whatever).

For this project, you can try the long context (PACKing) approach, or be ambitious and do RAG with a vector database.

⚠️⚠️⛔⛔ **IMPORTANT WARNING:** Don't feed the chatbot true proprietary data, such as your SSN or private information belonging to your employer. This data will end up in the OpenAI logs, and you *don't want that*. ⛔⛔⚠️⚠️

## Project 4: Build a Recipe App 👩‍🍳

Build an app that provides meal recipes! You can create this within the `recipe_app.py` file.

You'll find that an LLM can do this decently out of the box. However, to be production ready, consider the following things:

1. Does the app behave consistently? For example, does it always format the recipes in the same way each time? Does it ask the user the same types of clarifying questions each time?
2. The app should take a user's dietary restrictions into account.
3. The app should consider what ingredients the user currently has---or, at least, confirm whether the user is willing to go shopping to get the required ingredients.
4. The app should consider the user's taste preferences as well as current mood.
5. The app should know how many people are being served.
6. In the case where the user is willing to go shopping for ingredients, wouldn't it be cool if the app could provide a shopping list?
7. Feel free to add more criteria.

These are product decisions, and there's no one right way to make a recipe app. So, make these decisions quickly, and then focus on getting the app to behave according to spec.

## Project 5: Build a Podcast Producer 🎙️

You'll build an agent that produces actual audio podcasts for users.

I've set up some tools `podcast_tools.py` that you can equip your agent with. This includes:

* Write to file (simply creates a file on your filesystem)
* Web search (via [a specialized OpenAI tool](https://platform.openai.com/docs/guides/tools-web-search))
* Image generation (via [OpenAI's image model](https://platform.openai.com/docs/guides/tools-image-generation))
* Text-to-speech (via [OpenAI TTS](https://platform.openai.com/docs/guides/text-to-speech))

NOTE: The image generation capabilities may work only if ActiveCampaign has gone through a special verification process.

Now, build an agent that produces podcasts! The user can ask it to create a podcast based on any topic or current events. The agent should produce a transcript text file (.txt), an audio podcast (.mp3), and cover image (.png) for the podcast. Don’t build this all at once; add each bit of functionality one at a time. Starting with a transcript file is a good place to start.

Decide whether you want to create a classic agent (with or without a given plan), or if you'll go with an agentic workflow.

Bonus: Can you come up with some other agent you can build with these same tools? Also, feel free to add tools of your own!

## Project 6: Build a Coding Agent 🦾

Armed with Github MCP, let's create an agent that contributes to your favorite (or maybe least favorite) codebase. We can brainstorm exactly what this agent may look like, but here are some basic ideas:

* It can answer user questions about a codebase.
* It could try to resolve Github Issues, writing code and making pull requests.
* It can put a pull request through a code review.

