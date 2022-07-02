import { ResetComponent } from './email/reset/reset.component';
import { ForgotComponent } from './email/forgot/forgot.component';
import { ConfirmComponent } from './email/confirm/confirm.component';
import { RegisterComponent } from './register/register.component';
import { LoginComponent } from './login/login.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LogoutComponent } from './logout/logout.component';

const routes: Routes = [
  {
     path: '',
     component: LoginComponent,
     children:[{ path: 'login', component: LoginComponent, data: { pageTitle: 'Login' } }]
  },
  {
    path: '',
    component: RegisterComponent,
    children:[{ path: 'register', component: RegisterComponent, data: { pageTitle: 'Register' } }]
  },
  {
    path: '',
    component: LogoutComponent,
    children:[{ path: 'logout', component: LogoutComponent, data: { pageTitle: 'Logout' } }]
  },
  {
    path: 'email',
    component: ConfirmComponent,
    children:[{ path: 'confirm/:token', component: ConfirmComponent, data: { pageTitle: 'Confirmation' } }]
  },
  {
    path: 'email',
    component: ForgotComponent,
    children:[{ path: 'forgot', component: ForgotComponent, data: { pageTitle: 'Forgot Password' } }]
  },
  {
    path: 'email',
    component: ResetComponent,
    children:[{ path: 'reset/:token', component: ResetComponent, data: { pageTitle: 'Reset Password' } }]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AuthRoutingModule { }
