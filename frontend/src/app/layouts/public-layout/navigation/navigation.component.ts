import { Component, OnInit } from '@angular/core';
import{ GlobalConstants } from '../../../common/global-constants'

@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.scss']
})
export class NavigationComponent implements OnInit {

  title:string = GlobalConstants.SITE_NAME
  isAuth:boolean = true
  isAdmin:boolean = true

  constructor() { }

  ngOnInit(): void {
  }

}
