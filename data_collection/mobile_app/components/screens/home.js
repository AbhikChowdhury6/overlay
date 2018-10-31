import React, {Component} from 'react';
import {Image, TouchableOpacity, StyleSheet, Text, View, ScrollView, TextInput} from 'react-native';

export default class HomeScreen extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      latitude: null,
      longitude: null,
      error: null,
    }
  }

  static navigationOptions = ({navigation}) => {
    return {
      headerTitle: "Home",
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

  componentDidMount() {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        this.setState({
          latitude: position.coords.latitude,
          longitude: position.coords.longitude,
          error: null,
        })
      },
      (error) => this.setState({ error: error.message }),
      {enableHighAccuracy: false, timeout: 20000, maximumAge: 1000},
    );
    console.log(this.state);
  }

  render() {
    return (
      <View>
        <Text>Your location: {this.state.latitude}, {this.state.longitude}</Text>
        {this.state.error ? <Text>Error: {this.state.error}</Text> : null}
      </View>
    );
  }
}
