# Section 9 — the build

A short brief, not a tutorial. Once your prediction sheet is filled in and section 9 is ticked,
this is what closes it.

## What you are building

A small in-memory events API: one endpoint stores a short note, one lists what has been stored,
one fetches a single one by id.

## The interface

This much is fixed, and it is fixed so your submission can be checked by running it rather than
by reading it:

- `POST /events` with a JSON body `{"note": "<text>"}`, where `note` is 1 to 200 characters
  inclusive, returns `201` and a JSON body `{"id": <integer>, "note": "<text>"}`. Ids are
  assigned in increasing order, starting at 1.
- `GET /events` returns `200` and a JSON array of events, most recent first, each
  `{"id", "note"}`; `[]` when none have been stored yet. `?limit=<n>` caps how many come back;
  when `limit` is absent, the default is 10.
- `GET /events/{id}` returns `200` and that one event, or `404` with a JSON body carrying a
  `detail` key.
- A body that fails validation returns the framework's own `422`, in the framework's own shape.
  Write no validation code of your own for `note`'s type or length beyond the model itself.
- `GET /docs` answers `200`.
- Storage is in memory only.
- Every endpoint function is a plain `def`.
- The FastAPI instance is named `app`, in `app.py`, at the repository root, so that
  `python -m uvicorn app:app --port <port>` run from the root starts it.
- The repository root holds `app.py`, `requirements.txt` (pinned), and `NOTES.md`.

## What you are not building

No database, no Docker, no Compose, no CI, no tests required, no ORM, no auth.

## How this is marked

You are told this up front because it is not a trick: your submission is marked by starting it
with the command above and sending it requests. Every one of these is looked at, and nothing
else is.

- Every route in `app.py` is a plain `def`, not `async def`.
- The app starts and answers a request.
- A `POST /events` returns `201` with a body shaped exactly `{"id", "note"}`.
- Ids assigned across several posts come back in increasing order.
- `GET /events` lists what has been stored, most recent first.
- `?limit` caps the count, and the default applies when it is absent.
- `GET /events/{id}` for an id that exists returns that event.
- `GET /events/{id}` for an id that does not exist returns `404` with a `detail` key.
- A body that fails validation returns `422` in the framework's own shape, for every kind of
  invalid body the interface above describes.
- `GET /docs` answers `200`.

That is everything that is looked at. There is no eleventh thing, no hidden threshold, and no
partial credit for effort that does not show up in one of the ten above. Aim at the brief, not
at this list.

## The two conditions

The same two conditions as every build in this programme:

- Build it from an empty directory.
- Do not follow any single tutorial end to end.

## How long this should take

An evening or two. If it is taking longer, cut back to the interface above and say so on
Discord rather than pushing on quietly.

## Delivery

A new repository of your own — not this material repository — with the build on a feature
branch, delivered as a pull request. Put the pull request link in your section 9 completion
update on Discord, and bring it to your session. The repository's root holds exactly the layout
given in the interface above.

## `NOTES.md`

Three short paragraphs, one each on: what the model enforces on its own and what the framework
answers without you writing code for it; how ids and ordering are kept while the app is running,
and what that means the moment it restarts; and anything you could not get working. Treat this
file as the fourth column of your prediction sheet, written in prose instead of a table — an
honest account of what you did and did not manage, not a sales pitch for the code.

## This is the API half of the capstone

The capstone at the end of your checklist is a single larger project, built later. This build is
the shape of its API half, kept small and in memory on purpose. The capstone adds PostgreSQL in
place of the in-memory store, Docker and Compose to run the whole thing, a `pytest` suite, and a
GitHub Actions workflow that runs that suite on every push. Finishing this does not shorten the
capstone, and the capstone does not depend on anything here beyond the habit of building a small
API from an empty directory.
