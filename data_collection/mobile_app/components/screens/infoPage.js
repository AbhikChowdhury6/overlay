/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow
 */

 import React, { Component } from 'react';
 import { Text, View,TextInput, StyleSheet } from 'react-native';
 import {AppRegistry, Image, LinearGradient, Button, Alert, TouchableOpacity } from 'react-native';
 import ReusableTextBox from './ReusableTextBoxComp.js';


export default class InfoScreen extends Component<Props> {
  static navigationOptions = ({navigation}) => {
    return {
      headerTitle: "Log Info",
      headerRight: (
        <View/>
      ),
      headerLeft: (
        <TouchableOpacity onPress={() => navigation.openDrawer()}>
          <Image
            style={{width:40, height: 40}}
            source={require('./menu-512.png')}
          />
        </TouchableOpacity>
      )
    }
  }

  render() {
    return (
      <View style={styles.container}>
        <Text style = {styles.intro}>Enter user info below!!</Text>
        <ReusableTextBox
          placeholder='Type Weight'
          accessibilityLabel="Send Weight"
          onPress={()=>{Alert.alert('Weight Data Sent!!');}}
          />
        <ReusableTextBox
          placeholder='Type Blood Pressure'
          accessibilityLabel="Send Blood Pressure"
          onPress={()=>{Alert.alert('Blood Pressure Sent!!');}}
          />
        <ReusableTextBox
          placeholder='Type Body Temperature'
          accessibilityLabel ="Send Body Temperature"
          onPress={()=>{Alert.alert('Body Temperature Sent!!');}}
          />
        <ReusableTextBox
          placeholder='Type SPO2'
          accessibilityLabel="Send SPO2 Data"
          onPress={()=>{Alert.alert('SPO2 Data Sent!!');}}
         />
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'powderblue',
    //padding:20,
  },
  intro: {
    fontSize:30,
    textAlign: 'center',
    backgroundColor: 'powderblue',
    margin: 10,
    color: 'black',
  },
  picMe: {
    //alignItems: 'center',
    flex: 1,
    alignSelf: 'center',
    height: '45%',
    width: '100%',
    //resizeMode: 'cover',
    borderWidth: 0,
    borderRadius: 300,

  },
  inputfields: {
    alignSelf: 'flex-start',
    height: 60,
    width: 200,
    fontSize: 20,
    borderWidth: 1,
    color: 'black',
    borderColor: '#FFFF',
    margin: 10,
  },
  button: {
    marginBottom: 10,
    padding:20,
    width:100,
    height:30,
    justifyContent:'center',
  },
  textButtonsContainer: {

  },

});
