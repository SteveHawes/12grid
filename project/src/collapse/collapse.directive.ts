import { AfterViewInit, Directive, ElementRef, Renderer2 } from '@angular/core';

@Directive({ selector: '[gridCollapse]' })
export class CollapseDirective implements AfterViewInit {
    private showing = true;
    private height = 0;
    constructor(private elemRef: ElementRef, private renderer: Renderer2) {
    }
    ngAfterViewInit(): void {
        const element = this.elemRef.nativeElement as HTMLDivElement;
        let toggle = element.querySelector('.simple-collapsible-toggle');
        if (!toggle)
            toggle = element.querySelector('[data-toggle="collapse"]');
        let content = element.querySelector('.simple-collapsible-content');
        if (!content)
        	content = element.querySelector(toggle.getAttribute("data-target"));
        this.renderer.listen(toggle, 'click', () => {
            if (this.showing) {
                this.height = content.clientHeight;
                this.renderer.addClass(toggle, 'collapsed');
                this.renderer.removeClass(content, 'collapse');
                this.renderer.removeClass(content, 'show');
                this.renderer.addClass(content, 'collapsing');
                this.renderer.setStyle(content, 'height', this.height + 'px');
                setTimeout(() => {
                    this.renderer.setStyle(content, 'height', null);
                });
                setTimeout(() => {
                    this.renderer.removeClass(content, 'collapsing');
                    this.renderer.addClass(content, 'collapse');
                }, 300);
            } else {
                this.renderer.removeClass(toggle, 'collapsed');
                this.renderer.removeClass(content, 'collapse');
                this.renderer.addClass(content, 'collapsing');
                setTimeout(() => {
                    this.renderer.setStyle(content, 'height', this.height + 'px');
                });
                setTimeout(() => {
                    this.renderer.setStyle(content, 'height', null);
                    this.renderer.removeClass(content, 'collapsing');
                    this.renderer.addClass(content, 'collapse');
                    this.renderer.addClass(content, 'show');
                }, 300);
            }
            this.showing = !this.showing;
        });
        this.renderer.addClass(content, 'show');
    }

}
