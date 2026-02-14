PORTNAME=	brutemap
DISTVERSION=	65.da4b303
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Penetration testing tool that automates testing accounts to the sites login page.
WWW=		https://github.com/brutemap-dev/brutemap

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/geckodriver \
		??/py-argparse@${PY_FLAVOR} \
		??/py-backports.shutil_get_terminal_size@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-selenium@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
