//
//  ContentView.swift
//  EPQ app
//
//  Created by Paul Harper on 05/01/2025.
//

//!! settings

class globalSetings: ObservableObject {
    @Published var darkMode: Bool = false
    
}

//!! client code

import CoreBluetooth

class BLEPeripheralManager: NSObject, ObservableObject, CBPeripheralManagerDelegate {
    var peripheralManager: CBPeripheralManager!
    var transferCharacteristic: CBMutableCharacteristic!
    
    override init() {
        super.init()
        peripheralManager = CBPeripheralManager(delegate: self, queue: nil)
    }
    
    func peripheralManagerDidUpdateState(_ peripheral: CBPeripheralManager) {
        if peripheral.state == .poweredOn{
            let serviceUUID = CBUUID(string: "1234")
            let charUUID = CBUUID(string: "ABCD")
            
            transferCharacteristic = CBMutableCharacteristic(
                type: charUUID,
                properties: [.read,.notify],
                value: nil,
                permissions: [.readable]
            )
            
            let service = CBMutableService(type: serviceUUID, primary: true)
            service.characteristics = [transferCharacteristic]
            
            peripheralManager.add(service)
            peripheralManager.startAdvertising([
                CBAdvertisementDataServiceUUIDsKey: [serviceUUID],
                CBAdvertisementDataLocalNameKey: "MyBLEPeripheral"
            ])
        }
    }
    
    func updateValue(_ data:Data){
        guard let characteristic = transferCharacteristic else{
            print("transferCharacteristic is nil")
            return
        }
        peripheralManager.updateValue(data, for: characteristic, onSubscribedCentrals: nil)
    }
    
}

//!! display code

import SwiftUI

struct testingView:View {
    @State private var position_options: String = "Select a Position"
    @State private var timer_options: String = "Select a timer"
    @State var isPresenting = false
    @StateObject private var bleManager = BLEPeripheralManager()

    func client_connect(code:String){
        
        guard let data = code.data(using: .utf8) else{
            print("Failed to encode to UTF-8")
            return
        }
        bleManager.updateValue(data)
    }
    
    var body: some View {
        NavigationView{
            List{
                
                NavigationLink(destination: {
                    SettingsView()
                }, label: {Text(Image(systemName: "gear"))
                        .frame(maxWidth: .infinity, alignment:.trailing)
                }).disabled(true)
                
                Section() {
                    HStack(spacing:7,content:{
                        
                        Button(action:{client_connect(code: "Green")}) {
                            Text("Green Flag")
                        }
                        .buttonStyle(.bordered)
                        .tint(.green)
                        
                        Menu{
                            Button("position 1", action: {position_options="position 1";client_connect(code: "P1")})
                            Button("position 2", action: {position_options="position 2";client_connect(code: "P2")})
                            Button("position 3", action: {position_options="position 3";client_connect(code: "P3")})
                            Button("position 4", action: {position_options="position 4";client_connect(code: "P4")})
                        } label:{
                            Label(position_options,systemImage: "chevron.down")
                                .padding(7)
                                .background(Color.blue.opacity(0.1))
                                .cornerRadius(8)
                                .frame(maxWidth: .infinity, alignment: .trailing)
                        }
                    })
                    HStack(spacing:7,content:{
                        
                        Button(action:{client_connect(code: "Yellow")}){
                            Text("Yellow Flag")
                        }
                        .buttonStyle(.bordered)
                        .tint(.yellow)
                        
                        Menu{
                            Button("5 minutes", action: {timer_options="5 minutes";client_connect(code: "5M")})
                            Button("10 minutes", action: {timer_options="10 minutes";client_connect(code: "10M")})
                            Button("15 minutes", action: {timer_options="15 minutes";client_connect(code: "15M")})
                            Button("20 minutes", action: {timer_options="20 minutes";client_connect(code: "20M")})
                        } label:{
                            Label(timer_options,systemImage: "chevron.down")
                                .padding(7)
                                .background(Color.blue.opacity(0.1))
                                .cornerRadius(8)
                                .frame(maxWidth: .infinity, alignment: .trailing)
                        }
                    })
                    
                    HStack(spacing:7,content:{
                        
                        Button(action:{client_connect(code: "Red")}){
                            Text("Red Flag")
                        }
                        .buttonStyle(.bordered)
                        .tint(.red)
                    })
                    
                    HStack(spacing:7,content:{
                        Button(action:{client_connect(code: "Blue")}){
                            Text("Blue Flag")
                        }
                        .buttonStyle(.bordered)
                        .tint(.blue)
                    })
                }
            }
        }
    }
}
    
struct SettingsView:View {
    @EnvironmentObject var darkMode : globalSetings
    
    var body: some View {
        NavigationView{
            Form{
                Section(header: Text("Display"),
                        footer: Text("System settings will override Dark mode and use the current device theme")){
                    Toggle("Dark Mode", isOn: $darkMode.darkMode)
                        .onChange(of: darkMode.darkMode, initial: false) {oldValue, newValue in print("Dark mode changed from \(oldValue) to \(newValue)")}
                }
            }.navigationTitle("Settings")
            .preferredColorScheme(darkMode.darkMode ? .dark : .light)
        }
    }
}


//!! preview code

#Preview {
    testingView()
}
