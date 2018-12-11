//
//  ModeViewController.swift
//  Dehumidifier
//
//  Created by Patrick Johnson on 10/1/18.
//  Copyright © 2018 Patrick Johnson. All rights reserved.
//

import UIKit
import FirebaseAuth
import Firebase
import GoogleSignIn

class ModeViewController: UIViewController {
    @IBOutlet weak var capacityLabel: UILabel!
    @IBOutlet weak var humidityLabel: UILabel!
    let db = Firestore.firestore()
    var updateTimer: Timer!

   
    @IBOutlet weak var humiditySlider: UISlider!
    @IBOutlet weak var capacitySlider: UISlider!
    @IBOutlet weak var highEfficiencyMode: UISwitch!
    @IBOutlet weak var dehumidifyMode: UISwitch!
    @IBOutlet weak var hotWaterMode: UISwitch!
    @IBOutlet weak var logoutButton: UIButton!
    @IBOutlet weak var statsButton: UIButton!
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
        self.logoutButton.layer.cornerRadius = 23
        self.statsButton.layer.cornerRadius = 23
        
        let modeRef = db.collection("modes").document("mode")
        let humRef = db.collection("humidity").document("hum")
        let capRef = db.collection("capacity").document("cap")

        modeRef.getDocument { (document, error) in
            if let document = document, document.exists {
                let dataDescription = document.data()
                let result = (dataDescription?["value"] ?? 0) as! Int
                if(result == 0){
                    self.highEfficiencyMode.isOn = true
                    self.highEfficiencyMode.isEnabled = false
                    self.dehumidifyMode.isOn = false
                    self.hotWaterMode.isOn = false
                }else if(result == 1){
                    self.highEfficiencyMode.isOn = false
                    self.dehumidifyMode.isEnabled = false
                    self.dehumidifyMode.isOn = true
                    self.hotWaterMode.isOn = false
                }else if(result == 2){
                    self.highEfficiencyMode.isOn = false
                    self.hotWaterMode.isEnabled = false
                    self.dehumidifyMode.isOn = false
                    self.hotWaterMode.isOn = true
                }
            } else {
                print("Document does not exist")
            }
        }
        var capacityText = String(format: "%.1f", capacitySlider.value)
        capRef.getDocument { (document, error) in
            if let document = document, document.exists {
                let dataDescription = document.data()
                let result = (dataDescription?["value"] ?? 0) as! NSNumber
                self.capacitySlider.value = result.floatValue
                capacityText = String(format: "%.1f", result)
                self.capacityLabel.text = capacityText + " Gal"
                
            } else {
                print("Document does not exist")
            }
        }
        
        var val = humiditySlider.value * 100
        var humidityText = String(format: "%.1f", val)
        humRef.getDocument { (document, error) in
            if let document = document, document.exists {
                let dataDescription = document.data()
                let result = (dataDescription?["value"] ?? 0) as! NSNumber
                self.humiditySlider.value = result.floatValue/100
                val = result.floatValue
                humidityText = String(format: "%.1f", val)
                self.humidityLabel.text = humidityText + "%"
            } else {
                print("Document does not exist")
            }
        }
        startUpdate()
    }
    
    @IBAction func highEfficiencyEnabled(_ sender: Any) {
        self.dehumidifyMode.isEnabled = true
        self.dehumidifyMode.isOn = false
        self.hotWaterMode.isEnabled = true
        self.hotWaterMode.isOn = false
        self.highEfficiencyMode.isEnabled = false
        db.collection("modes").document("mode").setData([ "value": 0 ], merge: true) { err in
            if let err = err {
                print("Error writing document: \(err)")
            } else {
                print("Document successfully written!")
            }
        }
    }
    
    @IBAction func dehumidifyEnabled(_ sender: Any) {
        self.hotWaterMode.isEnabled = true
        self.hotWaterMode.isOn = false
        self.highEfficiencyMode.isEnabled = true
        self.highEfficiencyMode.isOn = false
        self.dehumidifyMode.isEnabled = false
        db.collection("modes").document("mode").setData([ "value": 1 ], merge: true) { err in
            if let err = err {
                print("Error writing document: \(err)")
            } else {
                print("Document successfully written!")
            }
        }
    }
    
    @IBAction func hotWaterEnabled(_ sender: Any) {
        self.dehumidifyMode.isEnabled = true
        self.dehumidifyMode.isOn = false
        self.highEfficiencyMode.isEnabled = true
        self.highEfficiencyMode.isOn = false
        self.hotWaterMode.isEnabled = false
        db.collection("modes").document("mode").setData([ "value": 2 ], merge: true) { err in
            if let err = err {
                print("Error writing document: \(err)")
            } else {
                print("Document successfully written!")
            }
        }

    }
    
    @IBAction func humidityChanged(_ sender: Any) {
       
        let val = humiditySlider.value * 100
        let humidityText = String(format: "%.1f", val)
        self.humidityLabel.text = humidityText + "%"
        db.collection("humidity").document("hum").setData([ "value": val ], merge: true) { err in
            if let err = err {
                print("Error writing document: \(err)")
            } else {
                print("Document successfully written!")
            }
        }
    }
    
    @IBAction func capacityChanged(_ sender: Any) {
        let capacityText = String(format: "%.1f", capacitySlider.value)
        self.capacityLabel.text = capacityText + " Gal"
        db.collection("capacity").document("cap").setData([ "value": capacitySlider.value ], merge: true) { err in
            if let err = err {
                print("Error writing document: \(err)")
            } else {
                print("Document successfully written!")
            }
        }
    }
    
    @IBAction func logoutAction(_ sender: Any) {
        
        do{
            try GIDSignIn.sharedInstance().signOut()
            try Auth.auth().signOut()
            try self.performSegue(withIdentifier: "logoutSegue", sender: self)
        }catch{
        
        }
    }
    
    func startUpdate(){
        updateTimer = Timer.scheduledTimer(timeInterval: 2, target: self, selector: #selector(updateFields), userInfo: nil, repeats: true)
        
    }
    
    @objc func updateFields(){
        let modeRef = db.collection("modes").document("mode")
        modeRef.getDocument { (document, error) in
            if let document = document, document.exists {
                let dataDescription = document.data()
                let result = (dataDescription?["value"] ?? 0) as! Int
                if(result == 0){
                    self.highEfficiencyMode.isOn = true
                    self.highEfficiencyMode.isEnabled = false
                    self.dehumidifyMode.isOn = false
                    self.hotWaterMode.isOn = false
                    self.dehumidifyMode.isEnabled = true
                    self.hotWaterMode.isEnabled = true
                }else if(result == 1){
                    self.highEfficiencyMode.isOn = false
                    self.dehumidifyMode.isEnabled = false
                    self.dehumidifyMode.isOn = true
                    self.hotWaterMode.isOn = false
                    self.highEfficiencyMode.isEnabled = true
                    self.hotWaterMode.isEnabled = true
                }else if(result == 2){
                    self.highEfficiencyMode.isOn = false
                    self.hotWaterMode.isEnabled = false
                    self.dehumidifyMode.isOn = false
                    self.hotWaterMode.isOn = true
                    self.dehumidifyMode.isEnabled = true
                    self.highEfficiencyMode.isEnabled = true
                }
            } else {
                print("Document does not exist")
            }
        }
        let humRef = db.collection("humidity").document("hum")
        let capRef = db.collection("capacity").document("cap")
        var capacityText = String(format: "%.1f", capacitySlider.value)
        capRef.getDocument { (document, error) in
            if let document = document, document.exists {
                let dataDescription = document.data()
                let result = (dataDescription?["value"] ?? 0) as! NSNumber
                self.capacitySlider.value = result.floatValue
                capacityText = String(format: "%.1f", result.floatValue)
                self.capacityLabel.text = capacityText + " Gal"
                
            } else {
                print("Document does not exist")
            }
        }
        
        var val = humiditySlider.value * 100
        var humidityText = String(format: "%.1f", val)
        humRef.getDocument { (document, error) in
            if let document = document, document.exists {
                let dataDescription = document.data()
                let result = (dataDescription?["value"] ?? 0) as! NSNumber
                self.humiditySlider.value = result.floatValue/100
                val = result.floatValue
                humidityText = String(format: "%.1f", val)
                self.humidityLabel.text = humidityText + "%"
            } else {
                print("Document does not exist")
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

}
