'use strict';

// =================================================================================
// App Configuration
// =================================================================================

const {App} = require('jovo-framework');

const config = {
    logging: true,
};

const app = new App(config);


// =================================================================================
// App Logic
// =================================================================================

app.setHandler({
    'LAUNCH': function() {
        this.toIntent('GreetingIntent');
    },

    'GreetingIntent': function() {
        this.tell('Hello everyone. Welcome to the dual use variable speed high efficiency dehumidifier presentation. My name is Alexa, and I will be assisting you today.');
    },

});

module.exports.app = app;
