import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  showPassword:boolean;
  password:string;
  credential:string;

  constructor() { }

 
  ngOnInit(): void {
  }

  toggleShow(event: any){
    this.showPassword = !this.showPassword
  }


  

}
