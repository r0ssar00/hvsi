%			if 'post' in globals():
				<div class="post type-post hentry category-uncategorized">
%               if 'view' in request.path:
					<div class="meta">
						{{post.time.day}} {{calendar.month_name[post.time.month]}} {{post.time.year}} @ {{post.time.strftime('%H:%M')}}
%					if request.admin:
						 // <a class="post-edit-link" href="/post/edit/{{post.id}}" title="{{i18n[lang]['post']['edit_entry']}}">{{i18n[lang]['post']['edit_entry']}}</a>
%					  if post.id > 5:
						 // <a class="post-edit-link" href="/post/delete/{{post.id}}" title="{{i18n[lang]['post']['delete_entry']}}">{{i18n[lang]['post']['delete_entry']}}</a>
%					  end
%					end
					</div>
%               end
%				if post.allow_comments:
					<div class="comment_count">
						<a class="comment_count_int" href="/post/view/{{post.id}}#respond" title="{{i18n[lang]['post']['comment']['on']}} {{getattr(post, 'title_' + lang)}}">{{post.comments.count()}}</a>
					</div>
%				end
%               if 'view' in request.path:
					<h1><a href="/post/view/{{post.id}}" rel="bookmark" title="{{i18n[lang]['post']['permalink']}} {{getattr(post, 'title_' + lang)}}">{{getattr(post, 'title_' + lang)}}</a></h1>
%               end

					<div class="body">
					%h=getattr(post, 'html_' + lang)
						<p>{{!h}}</p>
					</div>

				</div>
%			end
