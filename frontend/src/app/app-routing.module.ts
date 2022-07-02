import { AuthLayoutComponent } from './layouts/auth-layout/auth-layout.component';
import { PublicLayoutComponent } from './layouts/public-layout/public-layout.component';
import { AdminLayoutComponent } from './layouts/admin-layout/admin-layout.component';
import { ErrorLayoutComponent } from './layouts/error-layout/error-layout.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
    // Public Pages
    {
      path: '',
      component: PublicLayoutComponent,
      children: [
        {
            path: '',
            redirectTo: '/home',
            pathMatch: 'full'
        },
        {
            path: '',
            loadChildren: () => import('./pages/public/public.module').then(m => m.PublicModule)
        }
      ]
  },
  // Auth Pages
  {
    path: '',
    component: AuthLayoutComponent,
    children: [
      {
          path: '',
          redirectTo: '/auth',
          pathMatch: 'full'
      },
      {
          path: 'auth',
          loadChildren: () => import('./pages/auth/auth.module').then(m => m.AuthModule)
      }
    ]
 },
  // Admin Pages
   {
      path: '',
      component: AdminLayoutComponent,
      children: [
        {
            path: '',
            redirectTo: '/admin',
            pathMatch: 'full'
        },
        {
            path: 'admin',
            loadChildren: () => import('./pages/admin/admin.module').then(m => m.AdminModule)
        }
      ]
   },
   // Error Pages
   {
      path: '',
      component: ErrorLayoutComponent,
      children: [
        {
            path: '',
            redirectTo: '/error',
            pathMatch: 'full'
        },
        {
            path: 'error',
            loadChildren: () => import('./pages/error/error.module').then(m => m.ErrorModule)
        }
      ]
  },
  {path: '**', redirectTo: '/error/404'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
