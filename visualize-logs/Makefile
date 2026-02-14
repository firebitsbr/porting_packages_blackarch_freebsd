PORTNAME=	visualize-logs
DISTVERSION=	118.d2e370e
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Python library and command line tools to provide interactive log visualization.
WWW=		https://github.com/keithjjones/visualize_logs

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python

RUN_DEPENDS=	??/graphviz \
		??/jupyter-nbformat \
		??/py-networkx@${PY_FLAVOR} \
		??/py-pandas@${PY_FLAVOR} \
		??/py-plotly@${PY_FLAVOR} \
		??/py-pydotplus@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
