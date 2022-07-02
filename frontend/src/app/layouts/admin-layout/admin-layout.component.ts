import { Component, OnInit } from '@angular/core';
import{ GlobalConstants } from '../../common/global-constants'

@Component({
  selector: 'app-admin-layout',
  templateUrl: './admin-layout.component.html',
  styleUrls: ['./admin-layout.component.scss']
})
export class AdminLayoutComponent implements OnInit {

  title:string = GlobalConstants.SITE_NAME
  year:number = new Date().getFullYear()

  constructor() { }

  ngOnInit(): void {
  }

}
