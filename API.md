# SR Bot API description:

Each bot needs to provide 4 endpoints accessible trough http.

## POST ``hello`` endpoint

- Body parameter ``ApiHello``.
- ``Version`` should be checked, to ensure structure compatibility!
- Recommended way for now is to look only at ``map`` field, and not complicating the bot with community maps.
- Bot is required to provide response within 30 seconds. (A stricter limit might be introduced if needed.)
- Return type: ``AiForMapAPI``
  - ``name`` must be a constant returned on every call, no matter, what map is in the input
  - ``Decks`` is an array of decks that are supported on a map. If map is not supported, it will be empty.
- ``Wrapper.py`` simplifies this to:
  - ``decks_for_map`` function call with ``MapInfo`` as parameter, and ``List[DeckAPI]`` as return type while also ensuring the name to be ``None`` when not relevant.
  - It also sources the ``name`` from the implementation's property.

## POST ``prepare`` endpoint

- Body parameter ``APIPrepare``.
- It will contain a valid deck name provided by the ``hello`` endpoint, and map on which the match will happen.
- Bot is required to provide response within 30 seconds. (If bot needs any map based computations to prepare do it here.)
- Response no data, just http status code 200.
- ``Wrapper.py`` simplifies this to:
    - ``decks_for_map`` function call with ``MapInfo`` as parameter as with the ``hello`` endpoint.
    - It finds the requested deck, and calls ``prepare_for_battle`` with map, and deck information.

## POST ``start`` endpoint

- Body parameter ``APIGameStartState``.
- It will be called, when the match starts (tick 1).
- It contains ``your_player_id`` for the bot to recognize which entities belong to it.
- The player entities are not yet fully filled.
- Bot is required to respond within **90 ms**. (A penalization for causing delays will be determined later.)
- Response no data, just http status code 200.
- ``Wrapper.py`` simplifies this to:
    - ``match_start`` function call with the state, ``YourPlayerId`` and ``Entities``.

## POST ``tick`` endpoint

- Body parameter ``APIGameState``.
- It will be called on every tick.
- Respond with list of ``APICommand``s you want to do.
- Bot is required to respond within **50 ms**. (A penalization for causing delays will be determined later.)
- ``Wrapper.py`` simplifies this to:
    - ``tick`` function call with the state, ``CurrentTick`` and ``Entities``.
      - Later it might provide some local validation on commands, so you can get better understanding, instead of game just ignoring it.
      I plan to have this validation kind customizable (optional) to ease up development, while not costing any performance during real matches.
