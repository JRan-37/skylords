![Skylords Reborn Logo](https://gitlab.com/skylords-reborn/rust-libraries/-/blob/main/images/skylords_reborn_logo.png)

# Skylords Reborn Bot API Python

This repository contains an interface for bots to interact with the game BattleForge.

## Repo Structure

There are 2 subdirectories, and [API.md](./API.md).

### example

This directory contains two example bot implementations.
We recommend using this as base for your bot, and adding your own bot implementation.
The bot itself is executed via the entrypoint `run.py`.
The path to the bot implementation to run, as well as the port are given as command line arguments, e.g.

```python run.py example/example.py 7079```

If no port is specified, the default port 7079 will be used.

#### Dependencies

In order to run the example implementation, you need to install the packages listed in `requirements.txt`.
The easiest way to do this is by using `pip`:

```
pip install -r requirements.txt
```

### api

This directory contains the data types needed for communication with the game.

Optional feature is ``Wrapper.py`` that simplifies the implementation to a single AbsctractBaseClass.

### API.md

Explains how the api should work, and how the example api wrapper makes it easier to work with.

## You want to check other language?
- [Rust](https://gitlab.com/skylords-reborn/skylords-reborn-bot-api-rust)
- [C#](https://gitlab.com/skylords-reborn/skylords-reborn-bot-api-c-sharp)
- [Python](https://gitlab.com/skylords-reborn/skylords-reborn-bot-api-python)

## How to Contribute

Thank you for your interest in contributing to the Skylords Reborn Bot API Rust of Skylords Reborn.

To contribute to the source code, please follow these steps:

- Fork the repository and clone it locally.
- Create a short and descriptive branch in your fork.
- Commit and push your changes to that branch.
- Create a Merge Request to `main` from the repository. 
- Provide clear and concise titles to your merge requests. A merge request is not obliged to have an issue for now. Choose an appropriate template when creating your merge requests.
- When creating a merge request (MR), please mention the related issue, the changes made, and how to test it. If you have provided a detailed first commit message, these points will already be covered.
- Use the "Draft" status on MRs when relevant.
- Every merge request must be reviewed by at least one person before it is merged.
- Fix every compiler warning, as the compiler is always right. If you disagree, consult with someone before allowing a warning for a specific small part of the code and include the reasoning in the comment.
- Please use a linter such as `mypy` once in a while (or live within the IDE, if your computer can handle that) to reduce the amount of "clean-ups" needed.
- Please try to stick to `PEP 8` coding style conventions whenever possible
- Have a look around the source code to get a general sense of coding style. We prefer a pragmatic approach with this library.
- Depending on the number of contributions to this project, this process may be refined in the future.

For any questions, please contact [Metagross31](https://forum.skylords.eu/index.php?/profile/9568-metagross31/), or check out [discord](https://discord.com/channels/1158440761424089212/1158442837113831476).

## License

This project is open source and available under Boost Software License 1.0. See [LICENSE](./LICENSE) for more information.

## Disclosure
EA has not endorsed and does not support this product.
