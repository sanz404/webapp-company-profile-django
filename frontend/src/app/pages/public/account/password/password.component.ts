import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-password',
  templateUrl: './password.component.html',
  styleUrls: ['./password.component.scss']
})
export class PasswordComponent implements OnInit {

  showPassword:boolean;
  password:string;
  showPasswordConfirm:boolean;
  passwordConfirm:string;
  showPasswordOld:boolean;
  passwordOld:string;

  constructor() { }

  ngOnInit(): void {
  }

  toggleShow(event: any){
    this.showPassword = !this.showPassword
  }

  toggleShowConfirm(event: any){
    this.showPasswordConfirm = !this.showPasswordConfirm
  }

  toggleShowOld(event: any){
    this.showPasswordOld = !this.showPasswordOld
  }

}
