//
//  StatisticsViewController.swift
//  Dehumidifier
//
//  Created by Patrick Johnson on 10/1/18.
//  Copyright © 2018 Patrick Johnson. All rights reserved.
//

import UIKit
import FirebaseAuth
import Firebase

class StatisticsViewController: UIViewController {
    let db = Firestore.firestore()
    var updateTimer: Timer!

    @IBOutlet weak var cfmLabel: UILabel!
    @IBOutlet weak var waterCapacityLabel: UILabel!
    @IBOutlet weak var ovalButton: UIButton!
    @IBOutlet weak var waterTemp: UILabel!
    @IBOutlet weak var airTempLabel: UILabel!
    @IBOutlet weak var humidityLabel: UILabel!
    @IBOutlet weak var logoutButton: UIButton!
    @IBOutlet weak var controlsButton: UIButton!
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
        self.logoutButton.layer.cornerRadius = 23
        self.controlsButton.layer.cornerRadius = 23
        self.ovalButton.layer.borderWidth=2.5
        self.ovalButton.layer.cornerRadius = 23.0
        startUpdate()
    }
    @IBAction func logoutAction(_ sender: Any) {
        do{
            try Auth.auth().signOut()
            try self.performSegue(withIdentifier: "logoutSegue", sender: self)
        }catch{
            
        }
    }
    @objc func updateFields(){
        let docRef = db.collection("watertemps").document("watertemp")
        docRef.getDocument { (document, error) in
            if let document = document, document.exists {
                let temp = document.get("value") as! NSNumber
                let a = temp.floatValue
                self.waterTemp.text = String(a)+"°C"
            } else {
                print("Document does not exist")
            }
        }
        let humRef = db.collection("airhumidities").document("humidity")
        humRef.getDocument { (document, error) in
            if let document = document, document.exists {
                let hum = document.get("value") as! NSNumber
                let h = hum.floatValue
                self.humidityLabel.text = String(h)+"%"
            } else {
                print("Document does not exist")
            }
        }
        let airRef = db.collection("airtemps").document("airtemp")
        airRef.getDocument { (document, error) in
            if let document = document, document.exists {
                let aTemp = document.get("value") as! NSNumber
                let t = aTemp.floatValue
                self.airTempLabel.text = String(t)+"°C"
            } else {
                print("Document does not exist")
            }
        }
        let capRef = db.collection("waterCapacity").document("cap")
        capRef.getDocument { (document, error) in
            if let document = document, document.exists {
                let aTemp = document.get("value") as! NSNumber
                let t = aTemp.floatValue
                self.waterCapacityLabel.text = String(t)+" gal"
            } else {
                print("Document does not exist")
            }
        }
        
        let cfmRef = db.collection("cfm").document("cfm")
        cfmRef.getDocument { (document, error) in
            if let document = document, document.exists {
                let aTemp = document.get("value") as! NSNumber
                let t = aTemp.floatValue
                self.cfmLabel.text = String(t)+" CFM"
            } else {
                print("Document does not exist")
            }
        }
    }
    func startUpdate(){
        updateTimer = Timer.scheduledTimer(timeInterval: 1, target: self, selector: #selector(updateFields), userInfo: nil, repeats: true)

    }
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
