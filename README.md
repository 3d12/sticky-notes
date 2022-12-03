# sticky-notes

An example project integrating Flask and Svelte, based on a tutorial posted [`here`](https://www.twilio.com/blog/build-digital-sticky-notes-app-flask-svelte).

## Setup

In order to set up this project, there are a few things to do.

### Client Setup
1. Change directory to `client/` and run `npm install` -- this will install the dependencies for the **client** architecture.
2. Compile the **client** architecture, by running `npm run autobuild` from the `client/` folder. This creates the **.svelte-kit** directory which Flask serves from.

### Server Setup
1. Change directory to `server/` and run `python -m venv venv` to create a virtual environment, and `. venv/bin/activate` to activate it.
2. Run `python -m pip install -r requirements.txt` -- this will install the dependencies for the **server** architecture into your virtual environment.
3. From the server directory, with the virtual environment activated, run `flask --debug run` to start the server.
4. Connect on http://localhost:5000 and observe the majesty!

Credit to Mia Adjei for a terrific tutorial, all I did was update it to use the newest SvelteKit and removed the Twilio API integration.
