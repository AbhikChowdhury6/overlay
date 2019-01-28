import React, {Component} from 'react';
import {NavigationActions} from 'react-navigation';
import {View, TouchableOpacity, Text} from 'react-native';

export default class HamburgerMenu extends Component {
  componentWillMount(){

  }

  render() {
    return (
      <View>
        <View style={{ justifyContent: 'space-between', flexDirection: 'row' }}>
          <View>
            <Text>Menu</Text>
          </View>
          <View>
            <TouchableOpacity onPress={() => this.props.navigation.closeDrawer()}>
              <Text>x</Text>
            </TouchableOpacity>
          </View>
        </View>
        <View>
          <TouchableOpacity onPress={() => {this.props.navigation.closeDrawer()
                                            this.props.navigation.navigate('Info')}}>
            <Text>Info Screen</Text>
          </TouchableOpacity>
          <TouchableOpacity onPress={() => {this.props.navigation.closeDrawer()
                                            this.props.navigation.navigate('Mood')}}>
            <Text>Mood Screen</Text>
          </TouchableOpacity>
        </View>
      </View>
    );
  }
}
