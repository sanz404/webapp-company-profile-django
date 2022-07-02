import { Component, OnInit } from '@angular/core';
import{ GlobalConstants } from '../../../common/global-constants'

@Component({
  selector: 'admin-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.scss']
})
export class NavigationComponent implements OnInit {

  title:string = GlobalConstants.SITE_NAME
  totalNotif:number = Math.floor(Math.random() * 100)

  constructor() { }

  ngOnInit(): void {
  }

  toggleSideBar(event: any){
      let element = document.getElementById("admin-container");
      if(element){
          element.classList.toggle("sb-sidenav-toggled");
          let saved = document.body.classList.contains("sb-sidenav-toggled");
          localStorage.setItem('sb|sidebar-toggle', new Boolean(saved).toString())
      }
  }

}
