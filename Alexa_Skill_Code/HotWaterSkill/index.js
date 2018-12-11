'use strict';

const {Webhook} = require('jovo-framework');
const {app} = require('./app/app.js');

// =================================================================================
// Server Configuration
// =================================================================================

if (app.isWebhook()) {
    const port = process.env.PORT || 3000;
    Webhook.listen(port, () => {
        console.log(`Example server listening on port ${port}!`);
    });
    Webhook.post('/webhook', (req, res) => {
        app.handleWebhook(req, res);
    });
}
var firebase = require("firebase");

exports.handler = (event, context, callback) => {
    context.callbackWaitsForEmptyEventLoop = false;  //<---Important

    var config = {
        apiKey: "AIzaSyCPLF0_YuI-IQB9q0X2ZXn_yYbKTP1v_X8",
        authDomain: "mae4344-5859b.firebaseapp.com",
        databaseURL: "https://mae4344-5859b.firebaseio.com"
    };

    if(firebase.apps.length == 0) {   // <---Important!!! In lambda, it will cause double initialization.
        firebase.initializeApp(config);
    }
    app.handleLambda(event, context, callback);

};

