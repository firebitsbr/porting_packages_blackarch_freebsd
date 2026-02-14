PORTNAME=	deathstar
DISTVERSION=	60.d7bcbfd
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Automate getting Domain Admin using Empire.
WWW=		https://github.com/byt3bl33d3r/DeathStar

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-certifi@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-commonmark@${PY_FLAVOR} \
		??/py-h11@${PY_FLAVOR} \
		??/py-httpcore@${PY_FLAVOR} \
		??/py-httpx@${PY_FLAVOR} \
		??/py-idna@${PY_FLAVOR} \
		??/py-pygments@${PY_FLAVOR} \
		??/py-rfc3986@${PY_FLAVOR} \
		??/py-rich@${PY_FLAVOR} \
		??/py-sniffio@${PY_FLAVOR} \
		??/py-typing_extensions@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
