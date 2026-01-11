# Projects & Homework

The projects below are for Session #1. The projects for Session #2 will be added later.

## Project 1: LLM-Powered Functions 🛠️

1. Write a function that accepts a word and returns its opposite. (For example, if the input text is "top", the output would be "bottom".)
2. Write a function that accepts text and returns that same text with its grammar fixed.
3. Write a function that accepts a number written out in English, such as "one million, five hundred forty six thousand, two hundred and twenty two" and returns the equivalent integer.
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



