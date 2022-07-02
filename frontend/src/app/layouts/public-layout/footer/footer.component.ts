import { Component, OnInit } from '@angular/core';
import{ GlobalConstants } from '../../../common/global-constants'

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.scss']
})
export class FooterComponent implements OnInit {

  title:string = GlobalConstants.SITE_NAME
  year:number = new Date().getFullYear()

  constructor() { }

  ngOnInit(): void {
  }

}
