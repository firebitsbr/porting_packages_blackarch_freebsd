PORTNAME=	archivebox
DISTVERSION=	903.59da482
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	The open source self-hosted web archive. Takes browser history/bookmarks/Pocket/Pinboard/etc., saves HTML, JS, PDFs, media, and more.
WWW=		https://github.com/pirate/ArchiveBox

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/chromium \
		??/yt-dlp \
		devel/py-pip@${PY_FLAVOR} \
		ftp/wget \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
