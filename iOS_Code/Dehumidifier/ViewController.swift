//
//  ViewController.swift
//  Dehumidifier
//
//  Created by Patrick Johnson on 9/30/18.
//  Copyright © 2018 Patrick Johnson. All rights reserved.
//
import AudioToolbox
import UIKit
import Firebase
import GoogleSignIn

class ViewController: UIViewController, UITextFieldDelegate, UIGestureRecognizerDelegate, GIDSignInDelegate, GIDSignInUIDelegate{

    @IBOutlet weak var usernameLabel: UILabel!
    @IBOutlet weak var newAcctButton: UIButton!
    @IBOutlet weak var loginButton: UIButton!
    
    @IBOutlet weak var googleCustomButton: UIButton!
    @IBOutlet weak var errorMsg: UILabel!
    @IBOutlet weak var password: UITextField!
    @IBOutlet weak var usernameField: UITextField!
    override func viewDidLoad() {
        super.viewDidLoad()
        GIDSignIn.sharedInstance().uiDelegate = self
        GIDSignIn.sharedInstance().clientID = FirebaseApp.app()?.options.clientID
        GIDSignIn.sharedInstance().delegate = self
        self.googleCustomButton.layer.cornerRadius = 23
        self.usernameField.delegate = self
        self.password.delegate = self
        self.hideKeyboardWhenTappedAround()
        self.loginButton.layer.cornerRadius = 23
        self.newAcctButton.layer.cornerRadius = 23
        self.errorMsg.alpha = 0
        self.usernameField.layer.borderWidth=2.5
        self.usernameField.layer.cornerRadius = 15.0
        self.password.layer.borderWidth=2.5
        self.password.layer.cornerRadius = 15.0

    }
    @IBAction func googleCustomSignIn(_ sender: Any) {
        GIDSignIn.sharedInstance()?.signIn()
    }
    func sign(_ signIn: GIDSignIn!, didDisconnectWith user: GIDGoogleUser!, withError error: Error!) {
        // Perform any operations when the user disconnects from app here.
        // ...
    }
//    @IBAction func googlePressed(_ sender: Any) {
//        print("Here8")
//
//        GIDSignIn.sharedInstance().signIn()
//    }
    func sign(_ signIn: GIDSignIn!, didSignInFor user: GIDGoogleUser!, withError error: Error?) {
        if let error = error {
            // ...
            print(error)

            return
        }
    

        guard let authentication = user.authentication else { return }

        let credential = GoogleAuthProvider.credential(withIDToken: authentication.idToken,
                                                       accessToken: authentication.accessToken)
            Auth.auth().signInAndRetrieveData(with: credential) { (authResult, error) in
                if let error = error {
                    // ...
                    print("Here2")
                    return
                }
                self.performSegue(withIdentifier: "loginSegue", sender: self)

            }
        // ...
        
    }

    @available(iOS 9.0, *)
    func application(_ application: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any])
        -> Bool {
            return GIDSignIn.sharedInstance().handle(url,
                                                     sourceApplication:options[UIApplicationOpenURLOptionsKey.sourceApplication] as? String,
                                                     annotation: [:])
    }
    @IBAction func loginAction(_ sender: UIButton) {
        Auth.auth().signIn(withEmail: usernameField.text!, password: password.text!){ (user, error) in
            if(error != nil){
                UIView.animate(withDuration: TimeInterval(1.0), delay: TimeInterval(0.0), options: UIViewAnimationOptions.curveEaseIn, animations: {
                    self.errorMsg.alpha = 1.0}, completion: {
                        (finished: Bool) -> Void in
                        self.fadeOut()
                })
            AudioServicesPlayAlertSound(SystemSoundID(kSystemSoundID_Vibrate))
            }else{
                
                self.performSegue(withIdentifier: "loginSegue", sender: self)
            }
        }
    }
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    func textFieldShouldReturn(_ usernameField: UITextField) -> Bool {
        self.view.endEditing(true)
        return true
    }
    func textFieldShouldReturn2(_ password: UITextField) -> Bool {
        self.view.endEditing(true)
        return true
    }
    func fadeOut() {
        UIView.animate(withDuration: TimeInterval(2.0), delay: TimeInterval(0.0), options: UIViewAnimationOptions.curveEaseIn, animations: {
            self.errorMsg.alpha = 0.0
        }, completion: nil)
    }
    

    
}
extension UIViewController {
    func hideKeyboardWhenTappedAround() {
        let tap: UITapGestureRecognizer = UITapGestureRecognizer(target: self, action: #selector(UIViewController.dismissKeyboard))
        tap.cancelsTouchesInView = false
        view.addGestureRecognizer(tap)
    }
    
    @objc func dismissKeyboard() {
        view.endEditing(true)
    }
}

