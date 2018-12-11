'use strict';

// =================================================================================
// App Configuration
// =================================================================================

const {App} = require('jovo-framework');

const config = {
    logging: true,
};

const app = new App(config);

var admin = require("firebase-admin");

var serviceAccount = require("./firebase-admin.json");


admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://mae4344-5859b.firebaseio.com"
  });
var database = admin.firestore();
var modeRef;

// =================================================================================
// App Logic
// =================================================================================

app.setHandler({
    'LAUNCH': function() {
        this.toIntent('DehumidifyIntent');
    },

    'DehumidifyIntent': function() {

        modeRef = database.collection('modes').doc('mode');

        modeRef.set({
            value: 1
        }, {merge: true}).then(function() {
    console.log("Document successfully written!");
});

        this.tell('Engaging dehumidify mode');


    },
});

module.exports.app = app;
