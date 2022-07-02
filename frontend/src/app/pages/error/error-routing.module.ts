import { Page503Component } from './page503/page503.component';
import { Page500Component } from './page500/page500.component';
import { Page404Component } from './page404/page404.component';
import { Page403Component } from './page403/page403.component';
import { Page401Component } from './page401/page401.component';
import { Page400Component } from './page400/page400.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  { path: '', component: Page400Component, children:[{ path: '400', component: Page400Component, data: { pageTitle: 'Invalid request' } }] },
  { path: '', component: Page401Component, children:[{ path: '401', component: Page401Component, data: { pageTitle: 'Access Denied' } }] },
  { path: '', component: Page403Component, children:[{ path: '403', component: Page403Component, data: { pageTitle: 'Forbidden' } }] },
  { path: '', component: Page404Component, children:[{ path: '404', component: Page404Component, data: { pageTitle: 'This page Could Not Be Found' } }] },
  { path: '', component: Page500Component, children:[{ path: '500', component: Page500Component, data: { pageTitle: 'System Error' } }] },
  { path: '', component: Page503Component, children:[{ path: '503', component: Page503Component, data: { pageTitle: 'Access Denied' } }] },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ErrorRoutingModule { }
