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


//!! socket code
import SocketIO

func client_connect(code: String){
    let manager = SocketManager(socketURL: URL(string:"http://localhost:2325")!, config:[.log(true), .compress])
    let socket = manager.defaultSocket
    
    socket.on(clientEvent: .connect) {data, ack in print("socket connected")}

    socket.connect()
    
    if code == "Green" {
        socket.emit("chat message", "Green_flag")
    }
    
    if code == "Yellow" {
        socket.emit("chat message", "Yellow_flag")
    }
    
    if code == "Red"{
        socket.emit("chat message", "Red_flag")
    }
    
    if code == "Blue"{
        socket.emit("chat message", "Blue_flag")
    }
}


//!! display code

import SwiftUI

struct testingView:View {
    @State private var position_options: String = "Select a Position"
    @State private var timer_options: String = "Select a timer"
    @State var isPresenting = false
    
    var body: some View {
        NavigationView{
            List{
                
                NavigationLink(destination: {
                    SettingsView()
                }, label: {Text(Image(systemName: "gear"))
                        .frame(maxWidth: .infinity, alignment:.trailing)
                })
                
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

