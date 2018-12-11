//
//  RegisterViewController.swift
//  Dehumidifier
//
//  Created by Patrick Johnson on 10/2/18.
//  Copyright © 2018 Patrick Johnson. All rights reserved.
//
import AudioToolbox
import UIKit
import FirebaseAuth

class RegisterViewController: UIViewController {

    @IBOutlet weak var errorMsg: UILabel!
    @IBOutlet weak var passwordField: UITextField!
    @IBOutlet weak var usernameField: UITextField!
    @IBOutlet weak var registerButton: UIButton!
    @IBOutlet weak var homeButton: UIButton!
    override func viewDidLoad() {
        super.viewDidLoad()
        self.errorMsg.alpha = 0
        self.homeButton.layer.cornerRadius = 23
        self.registerButton.layer.cornerRadius = 23
        // Do any additional setup after loading the view.
    }
    @IBAction func goHome(_ sender: Any) {
        self.performSegue(withIdentifier: "goHome", sender: self)
    }
    @IBAction func registerAction(_ sender: UIButton){
        Auth.auth().createUser(withEmail: usernameField.text!, password: passwordField.text!){ (user, error) in
            if(error != nil){
                UIView.animate(withDuration: TimeInterval(1.0), delay: TimeInterval(0.0), options: UIViewAnimationOptions.curveEaseIn, animations: {
                    self.errorMsg.alpha = 1.0
                }, completion: {
                    (finished: Bool) -> Void in
                    self.fadeOut()
                })
                AudioServicesPlayAlertSound(SystemSoundID(kSystemSoundID_Vibrate))
            }else{
                self.performSegue(withIdentifier: "goHome", sender: self)
            }
        }
    }
    
    
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */
    func fadeOut() {
        UIView.animate(withDuration: TimeInterval(2.0), delay: TimeInterval(0.0), options: UIViewAnimationOptions.curveEaseIn, animations: {
            self.errorMsg.alpha = 0.0
        }, completion: nil)
    }
}

