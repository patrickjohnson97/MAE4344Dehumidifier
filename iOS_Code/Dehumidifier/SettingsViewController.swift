//
//  SettingsViewController.swift
//  Dehumidifier
//
//  Created by Patrick Johnson on 11/10/18.
//  Copyright © 2018 Patrick Johnson. All rights reserved.
//
import AudioToolbox
import UIKit
import Firebase

class SettingsViewController: UIViewController, UITextFieldDelegate, UIGestureRecognizerDelegate {


    @IBOutlet weak var email: UITextField!
    @IBOutlet weak var monthlySwitch: UISwitch!
    @IBOutlet weak var dailySwitch: UISwitch!
    @IBOutlet weak var safetySwitch: UISwitch!
    @IBOutlet weak var successText: UILabel!
    @IBOutlet weak var updateButton: UIButton!
    
    let db = Firestore.firestore()
    var updateTimer: Timer!

    override func viewDidLoad() {
        super.viewDidLoad()
        self.successText.alpha = 0.0;
        self.updateButton.layer.cornerRadius = 23;
        self.email.layer.borderWidth=2.5;
        self.email.layer.cornerRadius = 15.0;
        self.hideKeyboardWhenTappedAround()
        let safetyRef = db.collection("safety").document("safe")
        safetyRef.getDocument { (document, error) in
            if let document = document, document.exists {
                let dataDescription = document.data()
                let result = (dataDescription?["value"] ?? 0) as! Bool
                if(result){
                    self.safetySwitch.isOn = true;
                }else {
                    self.safetySwitch.isOn = false;
                }
            } else {
                print("Document does not exist")
            }
        }
        let dailyRef = db.collection("daily").document("day")
        dailyRef.getDocument { (document, error) in
            if let document = document, document.exists {
                let dataDescription = document.data()
                let result = (dataDescription?["value"] ?? 0) as! Bool
                if(result){
                    self.dailySwitch.isOn = true;
                }else {
                    self.dailySwitch.isOn = false;
                }
            } else {
                print("Document does not exist")
            }
        }
        let monthlyRef = db.collection("monthly").document("month")
        monthlyRef.getDocument { (document, error) in
            if let document = document, document.exists {
                let dataDescription = document.data()
                let result = (dataDescription?["value"] ?? 0) as! Bool
                if(result){
                    self.monthlySwitch.isOn = true;
                }else {
                    self.monthlySwitch.isOn = false;
                }
            } else {
                print("Document does not exist")
            }
        }
        let emailRef = db.collection("email").document("email")
        emailRef.getDocument { (document, error) in
            if let document = document, document.exists {
                let dataDescription = document.data()
                let result = (dataDescription?["value"] ?? 0) as! String
                self.email.text = result;
            } else {
                print("Document does not exist")
            }
        }
        // Do any additional setup after loading the view.
    }
    

    @IBAction func updatePressed(_ sender: Any) {
    AudioServicesPlayAlertSound(SystemSoundID(kSystemSoundID_Vibrate))
        UIView.animate(withDuration: TimeInterval(1.0), delay: TimeInterval(0.0), options: UIViewAnimationOptions.curveEaseIn, animations: {
            self.successText.alpha = 1.0
        }, completion: {
            (finished: Bool) -> Void in
            self.fadeOut()
        })
        db.collection("safety").document("safe").setData([ "value": safetySwitch.isOn ], merge: true) { err in
            if let err = err {
                print("Error writing document: \(err)")
            } else {
                print("Document successfully written!")
            }
        }
        db.collection("daily").document("day").setData([ "value": dailySwitch.isOn ], merge: true) { err in
            if let err = err {
                print("Error writing document: \(err)")
            } else {
                print("Document successfully written!")
            }
        }
        db.collection("monthly").document("month").setData([ "value": monthlySwitch.isOn ], merge: true) { err in
            if let err = err {
                print("Error writing document: \(err)")
            } else {
                print("Document successfully written!")
            }
        }
        db.collection("email").document("email").setData([ "value": email.text! ], merge: true) { err in
            if let err = err {
                print("Error writing document: \(err)")
            } else {
                print("Document successfully written!")
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
    func fadeIn(duration: TimeInterval = 1.0, delay: TimeInterval = 0.0, completion: @escaping ((Bool) -> Void) = {(finished: Bool) -> Void in}) {
        UIView.animate(withDuration: duration, delay: delay, options: UIViewAnimationOptions.curveEaseIn, animations: {
            self.successText.alpha = 1.0
        }, completion: completion)  }
    
    func fadeOut() {
        UIView.animate(withDuration: TimeInterval(2.0), delay: TimeInterval(0.0), options: UIViewAnimationOptions.curveEaseIn, animations: {
            self.successText.alpha = 0.0
        }, completion: nil)
    }
    func startUpdate(){
        updateTimer = Timer.scheduledTimer(timeInterval: 1, target: self, selector: #selector(updateFields), userInfo: nil, repeats: true)
        
    }
    
    @objc func updateFields(){
        let safetyRef = db.collection("safety").document("safe")
        safetyRef.getDocument { (document, error) in
            if let document = document, document.exists {
                let dataDescription = document.data()
                let result = (dataDescription?["value"] ?? 0) as! Bool
                if(result){
                    self.safetySwitch.isOn = true;
                }else {
                    self.safetySwitch.isOn = false;
                }
            } else {
                print("Document does not exist")
            }
        }
        let dailyRef = db.collection("daily").document("day")
        dailyRef.getDocument { (document, error) in
            if let document = document, document.exists {
                let dataDescription = document.data()
                let result = (dataDescription?["value"] ?? 0) as! Bool
                if(result){
                    self.dailySwitch.isOn = true;
                }else {
                    self.dailySwitch.isOn = false;
                }
            } else {
                print("Document does not exist")
            }
        }
        let monthlyRef = db.collection("monthly").document("month")
        monthlyRef.getDocument { (document, error) in
            if let document = document, document.exists {
                let dataDescription = document.data()
                let result = (dataDescription?["value"] ?? 0) as! Bool
                if(result){
                    self.monthlySwitch.isOn = true;
                }else {
                    self.monthlySwitch.isOn = false;
                }
            } else {
                print("Document does not exist")
            }
        }
        let emailRef = db.collection("email").document("email")
        emailRef.getDocument { (document, error) in
            if let document = document, document.exists {
                let dataDescription = document.data()
                let result = (dataDescription?["value"] ?? 0) as! String
                self.email.text = result;
            } else {
                print("Document does not exist")
            }
        }
    }
    
}

