PORTNAME=	badkarma
DISTVERSION=	85.2c46334
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Advanced network reconnaissance toolkit.
WWW=		https://github.com/r3vn/badKarma

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/ffmpeg \
		??/gtksourceview3 \
		??/mitmproxy \
		??/osm-gps-map \
		??/phantomjs \
		??/py-gobject@${PY_FLAVOR} \
		??/py-libnmap@${PY_FLAVOR} \
		??/py-shodan@${PY_FLAVOR} \
		??/py-sqlalchemy@${PY_FLAVOR} \
		??/vte3 \
		??/webkit2gtk \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
